# Quick start

## Installation

```bash
pip install google-custom-search
```

or if you use async version, please run this.

```bash
pip install google-custom-search[async]
```

## Example

### sync

```py
import google_custom_search


google = google_custom_search.CustomSearch(apikey="your api_key", engine_id="your engine_id")
# if image is True, it's can search, but you need to setting at google console search
results = google.search("Hello")
for result in results:
    # get a kind
    print(result.kind)
    
    # get a title.
    print(result.title)
  
    # get a link.
    print(result.url)
  
    # get a displayLink.
    print(result.display_url)
    
    # get a htmlTitle.
    print(result.html_title)
  
    # get a snippet.
    print(result.snippet)
```

### async

```py
from google_custom_search import CustomSearch, AiohttpAdapter
import asyncio


customsearch = CustomSearch(AiohttpAdapter("apikey", "engine"))


async def main():
    for item in await customsearch.search("python"):
        print(item.title)

asyncio.run(main())
```
