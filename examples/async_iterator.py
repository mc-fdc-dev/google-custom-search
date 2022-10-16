from google_custom_search import CustomSearch
import asyncio


customsearch = CustomSearch("apikey", "engineid")


async def main():
    async for item in customsearch.search_async_iterator:
        print(item.url)

asyncio.run(main())
