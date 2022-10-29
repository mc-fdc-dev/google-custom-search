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
from google_custom_search import CustomSearch, RequestsAdapter


customsearch = CustomSearch(RequestsAdapter("apikey", "engine_id"))
for item in customsearch.search("python"):
    print(item.url)
    print(item.title)
```

### async

```py
from google_custom_search import CustomSearch, AiohttpAdapter
import asyncio


customsearch = CustomSearch(AiohttpAdapter("apikey", "engine"))


async def main():
    for item in await customsearch.search("python"):
        print(item.url)
        print(item.title)

asyncio.run(main())
```
