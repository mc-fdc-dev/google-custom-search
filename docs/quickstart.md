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
import asyncio
import google_custom_search


google = google_custom_search.CustomSearch(token="your api_key", engine_id="your engine_id", image=True)
# if image is True, it's can search, but you need to setting at google console search
async def main():
    results = await google.search_async("word!")
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
    
asyncio.run(main())
```
