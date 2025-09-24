<p align="center">
  <img src="sphinx/_static/images/mcpswc.svg" alt="MCP Server Webcrawl" width="60%">
</p>

<p align="center">
  <a href="https://pragmar.com/mcp-server-webcrawl/" style="margin: 0 10px;">Website</a> |
  <a href="https://github.com/pragmar/mcp-server-webcrawl" style="margin: 0 10px;">GitHub</a> |
  <a href="https://pragmar.github.io/mcp-server-webcrawl/" style="margin: 0 10px;">Docs</a> |
  <a href="https://pypi.org/project/mcp-server-webcrawl/" style="margin: 0 10px;">PyPi</a>
</p>

# mcp-server-webcrawl

Advanced search and retrieval for web crawler data. With **mcp-server-webcrawl**, your AI client filters and analyzes web content under your direction or autonomously. The server includes a fulltext search interface with boolean support, and resource filtering by type, HTTP status, and more.

**mcp-server-webcrawl** provides the LLM a complete menu with which to search, and works with a variety of web crawlers:

| Crawler/Format | Description | Platforms | Setup Guide |
|---|---|---|---|
| [**ArchiveBox**][1] | Web archiving tool | macOS/Linux | [Setup Guide][8] |
| [**HTTrack**][2] | GUI mirroring tool | macOS/Windows/Linux | [Setup Guide][9] |
| [**InterroBot**][3] | GUI crawler and analyzer | macOS/Windows/Linux | [Setup Guide][10] |
| [**Katana**][4] | CLI security-focused crawler | macOS/Windows/Linux | [Setup Guide][11] |
| [**SiteOne**][5] | GUI crawler and analyzer | macOS/Windows/Linux | [Setup Guide][12] |
| [**WARC**][6] | Standard web archive format | varies by client | [Setup Guide][13] |
| [**wget**][7] | CLI website mirroring tool | macOS/Linux | [Setup Guide][14] |

[1]: https://archivebox.io
[2]: https://github.com/xroche/httrack
[3]: https://interro.bot
[4]: https://github.com/projectdiscovery/katana
[5]: https://crawler.siteone.io
[6]: https://en.wikipedia.org/wiki/WARC_(file_format)
[7]: https://en.wikipedia.org/wiki/Wget
[8]: https://pragmar.github.io/mcp-server-webcrawl/guides/archivebox.html
[9]: https://pragmar.github.io/mcp-server-webcrawl/guides/httrack.html
[10]: https://pragmar.github.io/mcp-server-webcrawl/guides/interrobot.html
[11]: https://pragmar.github.io/mcp-server-webcrawl/guides/katana.html
[12]: https://pragmar.github.io/mcp-server-webcrawl/guides/siteone.html
[13]: https://pragmar.github.io/mcp-server-webcrawl/guides/warc.html
[14]: https://pragmar.github.io/mcp-server-webcrawl/guides/wget.html

**mcp-server-webcrawl** is free and open source, and requires Claude Desktop and Python (>=3.10). It is installed on the command line, via pip install:

```bash
pip install mcp-server-webcrawl
```

For step-by-step MCP server setup, refer to the [Setup Guides](https://pragmar.github.io/mcp-server-webcrawl/guides.html).

## Features

* Claude Desktop ready
* Multi-crawler compatible
* Filter by type, status, and more
* Boolean search support
* Support for Markdown and snippets
* Roll your own website knowledgebase

## Prompt Routines

**mcp-server-webcrawl** provides the toolkit necessary to search web crawl data freestyle, figuring it out as you go, reacting to each query. This is what it was designed for.

It is also capable of running routines (as prompts). You can write these yourself, or use the ones provided. These prompts are **copy and paste**, and used as raw Markdown. They are enabled by the advanced search provided to the LLM; queries and logic can be embedded in a procedural set of instructions, or even an input loop as is the case with Gopher Service.

| Prompt | Download | Category | Description |
|--------|----------|----------|-------------|
|🔍 **SEO Audit** | [`auditseo.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/auditseo.md) | audit | Technical SEO (search engine optimization) analysis. Covers the basics, with options to dive deeper. |
|🔗 **404 Audit** | [`audit404.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/audit404.md) | audit | Broken link detection and pattern analysis. Not only finds issues, but suggests fixes. |
|⚡&nbsp;**Performance&nbsp;Audit** | [`auditperf.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/auditperf.md) | audit | Website speed and optimization analysis. Real talk. |
|📁 **File Audit** | [`auditfiles.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/auditfiles.md) | audit | File organization and asset analysis. Discover the composition of your website. |
|🌐 **Gopher Interface** | [`gopher.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/gopher.md) | interface | An old-fashioned search interface inspired by the Gopher clients of yesteryear. |
|⚙️ **Search Test** | [`testsearch.md`](https://raw.githubusercontent.com/pragmar/mcp-server-webcrawl/master/prompts/testsearch.md) | self-test | A battery of tests to check for Boolean logical inconsistencies in the search query parser and subsequent FTS5 conversion. |

If you want to shortcut the site selection (one less query), paste the markdown and in the same request, type "run pasted for [site name or URL]." It will figure it out. When pasted without additional context, you should be prompted to select from a list of crawled sites.

## Boolean Search Syntax

The query engine supports field-specific (`field: value`) searches and complex boolean expressions. Fulltext is supported as a combination of the url, content, and headers fields.

While the API interface is designed to be consumed by the LLM directly, it can be helpful to familiarize yourself with the search syntax. Searches generated by the LLM are inspectable, but generally collapsed in the UI. If you need to see the query, expand the MCP collapsible.

**Example Queries**

| Query Example | Description |
|--------------|-------------|
| privacy | fulltext single keyword match |
| "privacy policy" | fulltext match exact phrase |
| boundar* | fulltext wildcard matches results starting with *boundar* (boundary, boundaries) |
| id: 12345 | id field matches a specific resource by ID |
| url: example.com/somedir | url field matches results with URL containing example.com/somedir |
| type: html | type field matches for HTML pages only |
| status: 200 | status field matches specific HTTP status codes (equal to 200) |
| status: >=400 | status field matches specific HTTP status code (greater than or equal to 400) |
| content: h1 | content field matches content (HTTP response body, often, but not always HTML) |
| headers: text/xml | headers field matches HTTP response headers |
| privacy AND policy | fulltext matches both |
| privacy OR policy | fulltext matches either |
| policy NOT privacy | fulltext matches policies not containing privacy |
| (login OR signin) AND form | fulltext matches fulltext login or signin with form |
| type: html AND status: 200 | fulltext matches only HTML pages with HTTP success |

## Field Search Definitions

Field search provides search precision, allowing you to specify which columns of the search index to filter. Rather than searching the entire content, you can restrict your query to specific attributes like URLs, headers, or content body. This approach improves efficiency when looking for specific attributes or patterns within crawl data.

| Field | Description |
|-------|-------------|
| id | database ID |
| url | resource URL |
| type | enumerated list of types (see types table) |
| size | file size in bytes |
| status | HTTP response codes |
| headers | HTTP response headers |
| content | HTTP body—HTML, CSS, JS, and more |

## Field Content

A subset of fields can be independently requested with results, while core fields are always on. Use of headers and content can consume tokens quickly. Use judiciously, or use extras to crunch more results into the context window. Fields are a top level argument, independent of any field searching taking place in the query.

| Field | Description |
|-------|-------------|
| id | always available |
| url | always available |
| type | always available |
| status | always available |
| created | on request |
| modified | on request |
| size | on request |
| headers | on request |
| content | on request |

## Content Types

Crawls contain resource types beyond HTML pages. The `type:` field search allows filtering by broad content type groups, particularly useful when filtering images without complex extension queries. For example, you might search for `type: html NOT content: login` to find pages without "login," or `type: img` to analyze image resources. The table below lists all supported content types in the search system.

| Type | Description |
|------|-------------|
| html | webpages |
| iframe | iframes |
| img | web images |
| audio | web audio files |
| video | web video files |
| font | web font files |
| style | CSS stylesheets |
| script | JavaScript files |
| rss | RSS syndication feeds |
| text | plain text content |
| pdf | PDF files |
| doc | MS Word documents |
| other | uncategorized |

## Extras

The `extras` parameter provides additional processing options, transforming HTTP data (markdown, snippets, regex, xpath), or connecting the LLM to external data (thumbnails). These options can be combined as needed to achieve the desired result format.

| Extra | Description |
|-------|-------------|
| thumbnails | Generates base64 encoded images to be viewed and analyzed by AI models. Enables image description, content analysis, and visual understanding while keeping token output minimal. Works with images, which can be filtered using `type: img` in queries. SVG is not supported. |
| markdown | Provides the HTML content field as concise Markdown, reducing token usage and improving readability for LLMs. Works with HTML, which can be filtered using `type: html` in queries. |
| regex | Extracts regular expression matches from crawled files such as HTML, CSS, JavaScript, etc. Not as precise a tool as XPath for HTML, but supports any text file as a data source. One or more regex patterns can be requested, using the `extrasRegex` argument. |
| snippets | Matches fulltext queries to contextual keyword usage within the content. When used without requesting the content field (or markdown extra), it can provide an efficient means of refining a search without pulling down the complete page contents. Also great for rendering old school hit-highlighted results as a list, like Google search in 1999. Works with HTML, CSS, JS, or any text-based, crawled file. |
| xpath | Extracts XPath selector data, used in scraping HTML content. Use XPath's text() selector for text-only, element selectors return outerHTML. Only supported with `type: html`, other types will be ignored. One or more XPath selectors (//h1, count(//h1), etc.) can be requested, using the `extrasXpath` argument. |

Extras provide a means of producing token-efficient HTTP content responses. Markdown produces roughly 1/3 the bytes of the source HTML, snippets are generally 500 or so bytes per result, and XPath can be as specific or broad as you choose. The more focused your requests, the more results you can fit into your LLM session.

The idea, of course, is that the LLM takes care of this for you. If you notice your LLM developing an affinity to the "content" field (full HTML), a nudge in chat to budget tokens using the extras feature should be all that is needed.

## Interactive Mode

**No AI, just classic Boolean search of your web-archives in a terminal.**

mcp-server-webcrawl can double as a terminal search for your web archives. You can run it against your local archives, but it gets more interesting when you realize you can ssh into any remote host and view archives sitting on that host. No downloads, syncs, multifactor logins, or other common drudgery required. With interactive mode, you can be in and searching a crawl sitting on a remote server in no time at all.

Launch with --crawler and --datasource to load into search immediately, or use setup datasrc and crawler in-app.

```bash
mcp-server-webcrawl --crawler wget --datasrc /path/to/datasrc --interactive
# or manually enter crawler and datasrc in the UI
mcp-server-webcrawl --interactive
```

Interactive mode is a way to search through tranches of crawled data, whenever, whereever... in a terminal.

![Interactive search interface](sphinx/_static/images/interactive.search.webp)