import anyio
import re
import sqlite3
import traceback

from pathlib import Path
from typing import Any, Callable, Final
from urllib.parse import urlparse

from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.types import EmbeddedResource, ImageContent, TextContent, Tool

from mcp_server_webcrawl.crawlers.base.api import BaseJsonApi
from mcp_server_webcrawl.crawlers.base.adapter import IndexState
from mcp_server_webcrawl.models import METADATA_VALUE_TYPE
from mcp_server_webcrawl.models.sites import SITES_TOOL_NAME
from mcp_server_webcrawl.models.resources import (
    ResourceResult,
    ResourceResultType,
    RESOURCES_DEFAULT_FIELD_MAPPING,
    RESOURCES_DEFAULT_SORT_MAPPING,
    RESOURCE_EXTRAS_ALLOWED,
    RESOURCES_TOOL_NAME,
)
from mcp_server_webcrawl.extras.thumbnails import ThumbnailManager
from mcp_server_webcrawl.extras.markdown import get_markdown
from mcp_server_webcrawl.extras.regex import get_regex
from mcp_server_webcrawl.extras.snippets import get_snippets
from mcp_server_webcrawl.extras.xpath import get_xpath

from mcp_server_webcrawl.utils.logger import get_logger

OVERRIDE_ERROR_MESSAGE: Final[str] = """BaseCrawler subclasses must implement the following \
methods: handle_list_tools, handle_call_tool, at minimum."""

logger = get_logger()


class BaseCrawler:
    """
    Base crawler class that implements MCP server functionality.

    This class provides the foundation for specialized crawlers to interact with
    the MCP server and handle tool operations for web resources.
    """

    def __init__(
        self,
        datasrc: Path,
        get_sites_func: Callable,
        get_resources_func: Callable,
        resource_field_mapping: dict[str, str] = RESOURCES_DEFAULT_FIELD_MAPPING,
    ) -> None:
        """
        Initialize the BaseCrawler with a data source path and required adapter functions.

        Args:
            datasrc: path to the data source
            get_sites_func: function to retrieve sites from the data source
            get_resources_func: function to retrieve resources from the data source
            resource_field_mapping: mapping of resource field names to display names
        """

        from mcp_server_webcrawl import __name__ as module_name, __version__ as module_version

        assert datasrc is not None, f"{self.__class__.__name__} needs a datasrc, regardless of action"
        assert callable(get_sites_func), f"{self.__class__.__name__} requires a callable get_sites_func"
        assert callable(get_resources_func), f"{self.__class__.__name__} requires a callable get_resources_func"
        assert isinstance(resource_field_mapping, dict), f"{self.__class__.__name__} resource_field_mapping must be a dict"

        self._datasrc: Path = Path(datasrc)

        self._module_name: str = module_name
        self._module_version: str = module_version

        self._server = Server(self._module_name)
        self._server.list_tools()(self.mcp_list_tools)
        self._server.call_tool()(self.mcp_call_tool)
        self._server.list_prompts()(self.mcp_list_prompts)
        self._server.list_resources()(self.mcp_list_resources)

        self._resource_field_mapping = resource_field_mapping
        self._adapter_get_sites = get_sites_func
        self._adapter_get_resources = get_resources_func

    @property
    def datasrc(self) -> Path:
        return self._datasrc

    async def mcp_list_prompts(self) -> list:
        """List available prompts (currently none)."""
        return []

    async def mcp_list_resources(self) -> list:
        """List available resources (currently none)."""
        return []

    async def serve(self, stdin: anyio.AsyncFile[str] | None, stdout: anyio.AsyncFile[str] | None) -> dict[str, Any]:
        """
        Launch the awaitable server.

        Args:
            stdin: input stream for the server
            stdout: output stream for the server

        Returns:
            The MCP server over stdio
        """
        return await self._server.run(stdin, stdout, self.get_initialization_options())

    def get_initialization_options(self) -> InitializationOptions:
        """
        Get the MCP initialization object.

        Returns:
            Dictionary containing project information
        """
        notification_events = NotificationOptions(prompts_changed=False, resources_changed=False, tools_changed=False)
        capabilities = self._server.get_capabilities(notification_options=notification_events, experimental_capabilities={})
        return InitializationOptions(server_name=self._module_name, server_version=self._module_version, capabilities=capabilities)

    def get_sites_api_json(self, **kwargs) -> str:
        """
        Get sites API result as JSON.

        Returns:
            JSON string of sites API results
        """
        json_result = self.get_sites_api(**kwargs)
        return json_result.to_json()

    def get_resources_api_json(self, **kwargs) -> str:
        """
        Get resources API result as JSON.

        Returns:
            JSON string of resources API results
        """
        json_result = self.get_resources_api(**kwargs)
        return json_result.to_json()

    def get_sites_api(
            self,
            ids: list[int] | None = None,
            fields: list[str] | None = None,
    ) -> BaseJsonApi:
        sites = self._adapter_get_sites(self._datasrc, ids=ids, fields=fields)
        sites_kwargs = {
            "ids": ids,
            "fields": fields,
        }
        json_result = BaseJsonApi("GetProjects", sites_kwargs)
        json_result.set_results(sites, len(sites), 0, len(sites))
        return json_result

    def get_resources_api(
        self,
        sites: list[int] | None = None,
        query: str = "",
        fields: list[str] | None = None,
        sort: str | None = None,
        limit: int = 20,
        offset: int = 0,
        extras: list[str] | None = None,
        extrasRegex: list[str] | None = None,
        extrasXpath: list[str] | None = None,
    ) -> BaseJsonApi:
        resources_kwargs: dict[str, METADATA_VALUE_TYPE] = {
            "sites": sites,
            "query": query,
            "fields": fields,
            "sort": sort,
            "limit": limit,
            "offset": offset,
        }

        def no_results() -> BaseJsonApi:
            api_result = BaseJsonApi("GetResources", resources_kwargs, index_state=IndexState())
            api_result.set_results([], 0, 0, limit)
            return api_result

        if not sites:
            all_sites = self._adapter_get_sites(self._datasrc)
            if not all_sites:
                return no_results()
            # set to default of all sites if not specified
            sites = [site.id for site in all_sites]

        # sometimes the AI gets it in its head this is a good idea
        # but it means no query, just take care of it here
        if query.strip() in ('""',"''", "``", "*"):
            query = ""

        site_matches = self._adapter_get_sites(self._datasrc, ids=sites)
        if not site_matches:
            return no_results()

        extras = extras or []
        extrasXpath = extrasXpath or []
        extrasRegex = extrasRegex or []
        fields = fields or []
        fields_extras_override: list[str] = fields.copy()

        set_extras: set[str] = set(extras)
        set_extras_content: set[str] = {"markdown", "snippets", "xpath", "regex"}
        set_extras_headers: set[str] = {"snippets", "regex"}
        add_content: bool = bool(set_extras_content & set_extras)
        add_headers: bool = bool(set_extras_headers & set_extras)

        if add_content and "content" not in fields:
            fields_extras_override.append("content")

        if add_headers and "headers" not in fields:
            fields_extras_override.append("headers")

        results, total, index_state = self._adapter_get_resources(
            self._datasrc,
            sites=sites,
            query=query,
            fields=fields_extras_override,
            sort=sort,
            limit=limit,
            offset=offset,
        )

        if "markdown" in extras:
            result: ResourceResult
            for result in results:
                markdown_result: str | None = None
                if result.type == ResourceResultType.PAGE:
                    markdown_result = get_markdown(result.content)
                result.set_extra("markdown", markdown_result)

        if "xpath" in extras:
            result: ResourceResult
            for result in results:
                xpath_result: list[dict[str, str | int | float]] = get_xpath(result.content, extrasXpath)
                result.set_extra("xpath", xpath_result)

        if "regex" in extras:
            result: ResourceResult
            for result in results:
                regex_result: list[dict[str, str | int | float]] = get_regex(result.headers, result.content, extrasRegex)
                result.set_extra("regex", regex_result)

        if "snippets" in extras and query.strip():
            result: ResourceResult
            for result in results:
                snippets: str | None = get_snippets(result.url, result.headers, result.content, query)
                result.set_extra("snippets", snippets)

        extras_only_fields = set(fields_extras_override) - set(fields)
        if extras_only_fields:
            for result in results:
                for field in extras_only_fields:
                    if hasattr(result, field):
                        setattr(result, field, None)

        # note: thumbnails extra a special case, handled in mcp_call_tool
        api_result = BaseJsonApi("GetResources", resources_kwargs, index_state=index_state)
        api_result.set_results(results, total, offset, limit)
        return api_result

    async def mcp_list_tools(self) -> list[Tool]:
        """
        List available tools.

        Returns:
            List of available tools

        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        # each crawler subclass must provide this method
        raise NotImplementedError(OVERRIDE_ERROR_MESSAGE)

    async def mcp_call_tool(self, name: str, arguments: dict[str, Any] | None
        ) -> list[TextContent | ImageContent | EmbeddedResource]:
        """
        Handle tool execution requests. You can override this or super(), then tweak.
        Basically, it is a passthrough.

        Args:
            name: name of the tool to call
            arguments: arguments to pass to the tool

        Returns:
            List of content objects resulting from the tool execution

        Raises:
            ValueError: If the specified tool does not exist
        """
        try:
            if name == SITES_TOOL_NAME:
                ids: list[int] = [] if not arguments or "ids" not in arguments else arguments["ids"]
                fields: list[str] = [] if not arguments or "fields" not in arguments else arguments["fields"]

                assert isinstance(ids, list) and all(isinstance(item, int) for item in ids)
                assert isinstance(fields, list) and all(isinstance(item, str) for item in fields)

                results_json = self.get_sites_api_json(
                    ids=ids,
                    fields=fields
                )
                return [TextContent(type="text", text=results_json)]

            elif name == RESOURCES_TOOL_NAME:

                extras: list[str] = [] if not arguments or "extras" not in arguments else arguments["extras"]

                # in case there is any LLM confusion of XPath/xpath or Markdown/markdown, these are
                # defined lowercase in the MCP Tool definition, but have counter-weighting as proper nouns
                extras = [extra.lower() for extra in extras if isinstance(extra, str)]
                extrasRegex: list[str] = [] if not arguments or "extrasRegex" not in arguments else arguments["extrasRegex"]
                extrasXpath: list[str] = [] if not arguments or "extrasXpath" not in arguments else arguments["extrasXpath"]

                extras_set: set[str] = set(extras)
                extras_removed: set[str] = extras_set - RESOURCE_EXTRAS_ALLOWED
                if extras_removed:
                    # only allow known extras
                    extras = list(RESOURCE_EXTRAS_ALLOWED.intersection(extras))

                # regular args pass through to the result
                query: str = "" if not arguments or "query" not in arguments else arguments["query"]
                fields: list[str] = [] if not arguments or "fields" not in arguments else arguments["fields"]
                sites: list[int] = [] if not arguments or "sites" not in arguments else arguments["sites"]
                sort: str | None = None if not arguments or "sort" not in arguments else arguments["sort"]
                limit: int = 20 if not arguments or "limit" not in arguments else arguments["limit"]
                offset: int = 0 if not arguments or "offset" not in arguments else arguments["offset"]

                # claude keeps getting this wrong, it is properly enumerated in Tool definition
                clean_sort = sort.strip("\"'`") if isinstance(sort, str) else None

                assert isinstance(query, str)
                assert isinstance(fields, list) and all(isinstance(item, str) for item in fields)
                assert isinstance(sites, list) and all(isinstance(item, int) for item in sites)
                assert isinstance(sort, (str, type(None)))
                assert isinstance(limit, int)
                assert isinstance(offset, int)
                assert isinstance(extras, list) and all(isinstance(item, str) for item in extras)
                assert isinstance(extrasXpath, list) and all(isinstance(item, str) for item in extrasXpath)

                api_result: BaseJsonApi = self.get_resources_api(
                    sites=sites,
                    query=query,
                    fields=fields,
                    sort=clean_sort,
                    limit=limit,
                    offset=offset,
                    extras=extras,
                    extrasRegex=extrasRegex,
                    extrasXpath=extrasXpath,
                )
                # sometimes nudging makes things worse, AI doubles down on percieved
                # rightousness of position. just let it have it. claims in the end it's
                # a JSON encoding confusion with the +/- leading char. who knows? more
                # importantly, who cares? play it loose.
                # if sort != clean_sort:
                #     # let the MCP host know the error of its ways
                #     api_result.append_error(f"invalid sort ({sort}) requested [{', '.join(RESOURCES_DEFAULT_SORT_MAPPING.keys())}]")
                if extras_removed:
                    # only allow known extras
                    api_result.append_error(f"invalid extras requested ({', '.join(extras_removed)})")


                crawl_results: list[ResourceResult] = api_result.get_results()
                results_json = api_result.to_json()
                mcp_result = [TextContent(type="text", text=results_json)]

                if "thumbnails" in extras:
                    crawl_results: list[ResourceResult] = api_result.get_results()
                    mcp_result += self.get_thumbnails(crawl_results) or []

                return mcp_result
            else:
                raise ValueError(f"No such tool ({name})")

        except sqlite3.Error as ex:
            return [TextContent(type="text", text=f"mcp_call_tool/database\n{str(ex)}\n{traceback.format_exc()}")]
        except Exception as ex:
            return [TextContent(type="text", text=f"mcp_call_tool/exception\n{str(ex)}\n{traceback.format_exc()}")]

    def get_thumbnails(self, results: list[ResourceResult]) -> list[ImageContent]:

        thumbnails_result: list[ImageContent] = []
        image_paths = list(set([result.url for result in results if result.url and
                result.type == ResourceResultType.IMAGE]))
        valid_paths = []
        for path in image_paths:
            parsed = urlparse(path)
            if parsed.scheme in ("http", "https") and parsed.netloc:
                clean_path: str = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                valid_paths.append(clean_path)
            elif re.search(r"\.(jpg|jpeg|png|gif|bmp|webp)$", path, re.IGNORECASE):
                clean_path: str = path.split("?")[0]
                valid_paths.append(clean_path)

        if valid_paths:
            try:
                thumbnail_manager = ThumbnailManager()
                thumbnail_data = thumbnail_manager.get_thumbnails(valid_paths)
                for thumbnail_url, thumbnail_base64 in thumbnail_data.items():
                    if thumbnail_base64 is None:
                        logger.debug(f"Thumbnail encountered error during request. {thumbnail_url}")
                        continue
                    image_content = ImageContent(type="image", data=thumbnail_base64, mimeType="image/webp")
                    thumbnails_result.append(image_content)
                logger.debug(f"Fetched {len(thumbnail_data)} thumbnails out of {len(valid_paths)} requested URLs")
            except Exception as ex:
                logger.error(f"Error fetching thumbnails: {ex}\n{traceback.format_exc()}")

        return thumbnails_result

    def _convert_to_resource_types(self, types: list[str] | None) -> list[ResourceResultType] | None:
        """
        Convert string type values to ResourceResultType enums.  Silently ignore invalid type strings.

        Args:
            types: optional list of string type values

        Returns:
            Optional list of ResourceResultType enums, or None if no valid types
        """
        if not types:
            return None

        result = [rt for rt in ResourceResultType if rt.value in types]
        return result if result else None

