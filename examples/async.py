from google_custom_search import CustomSearch, AiohttpAdapter
import asyncio


customsearch = CustomSearch(AiohttpAdapter("apikey", "engine"))


async def main():
    for item in await customsearch.search("python"):
        print(item.title)

asyncio.run(main())
