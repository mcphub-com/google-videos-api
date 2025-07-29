```markdown
# Aigeon AI Google Videos API

Aigeon AI Google Videos API is a Python-based server application designed to interact with the Google Videos API through SerpAPI. This server facilitates video searches on Google, providing structured data about video results, including titles, links, thumbnails, and durations. The application is built using the FastMCP framework, ensuring efficient and scalable server operations.

## Features Overview

- **Google Video Search**: Leverage the power of Google Videos API to perform video searches with advanced query capabilities.
- **Structured Data Output**: Receive structured data containing video details such as title, link, thumbnail, and duration.
- **Customizable Search Parameters**: Fine-tune search results using various parameters like location, language, device type, and more.
- **Safe Search Filtering**: Option to enable or disable adult content filtering.
- **Pagination Support**: Retrieve multiple pages of results with pagination controls.
- **Cache Management**: Control caching behavior to optimize performance or ensure fresh data retrieval.
- **Asynchronous Mode**: Option to perform searches asynchronously for improved performance.

## Main Features and Functionality

The Aigeon AI Google Videos API server provides a single main function, `search_videos`, which is exposed as a tool through the FastMCP server. This function allows users to perform video searches with a wide range of customizable parameters. Key functionalities include:

- **Advanced Query Syntax**: Support for advanced search queries including operators like `inurl:`, `site:`, `intitle:`, etc.
- **Location-Based Searches**: Specify geographic locations to tailor search results to a specific area.
- **Domain and Language Customization**: Customize the Google domain and language settings to suit specific needs.
- **Search Filters**: Apply various filters to refine search results based on language, date, duration, and more.
- **Device Type Specification**: Choose between desktop, tablet, or mobile to simulate different user experiences.
- **Result Quantity Control**: Define the number of results returned per search, ranging from 10 to 100.
- **Error Handling**: Robust error handling to manage HTTP errors effectively.

## Main Functions Description

### `search_videos`

The `search_videos` function is the core of the Aigeon AI Google Videos API server, providing a comprehensive interface for querying Google Videos. Below is a detailed description of its parameters:

- **q**: *(str)* - The search query content, supporting advanced syntax like `inurl:`, `site:`, `intitle:`, etc.
- **location**: *(Union[str, None])* - Geographical location for search precision (e.g., 'Austin, TX').
- **uule**: *(Union[str, None])* - Google encoded location, mutually exclusive with `location`.
- **google_domain**: *(Union[str, None])* - Google domain to use, defaults to 'google.com'.
- **gl**: *(Union[str, None])* - Country code for localization (e.g., 'us' for the USA).
- **hl**: *(Union[str, None])* - Language code for the search (e.g., 'en' for English).
- **lr**: *(Union[str, None])* - Restrict search to specific languages (e.g., 'lang_fr|lang_de').
- **tbs**: *(Union[str, None])* - Advanced search parameters for filtering by date, duration, etc.
- **safe**: *(Union[Literal["active", "off"], None])* - Safe search filter, 'active' or 'off'.
- **nfpr**: *(Union[int, None])* - Exclude spelling correction results (1=yes, 0=no).
- **filter**: *(Union[int, None])* - Enable or disable result filtering (1=enabled, 0=disabled).
- **start**: *(Union[int, None])* - Pagination offset (e.g., 0=first page, 10=second page).
- **num**: *(Union[int, None])* - Number of results to return (10-100).
- **device**: *(Union[Literal["desktop", "tablet", "mobile"], None])* - Device type for search.
- **no_cache**: *(Union[bool, None])* - Disable caching if set to True.
- **async_mode**: *(Union[bool, None])* - Enable asynchronous result fetching, requires Searches Archive API.

This function constructs a request payload based on the provided parameters, sends a request to the SerpAPI, and returns the JSON response containing the search results.

---

This README provides a comprehensive overview of the Aigeon AI Google Videos API server, detailing its features, functionality, and usage. For further information or support, please refer to the project's documentation or contact the development team.
```