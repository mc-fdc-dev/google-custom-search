import requests
try:
    import aiohttp
except ImportError:
    no_async = True
else:
    no_async = False

from typing import Optional, List, AsyncIterator
from .errors import ApiNotEnabled, AsyncError
from .types import Item


class CustomSearch:
    """This is the class used when using Google Custom Search.

    Args:
        apikey (str): Insert google custom search api key.
        engine_id (str): Insert google custom search engine id.
    """
    APIURL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self,
                 apikey: str,
                 engine_id: str,
                 image: Optional[bool] = False):
        self.token = apikey
        self.engine_id = engine_id
        self.image = image

    def search(self, keyword: str) -> List[Item]:
        """This is searched using api.

        Args:
            keyword (str): Search word

        Returns:
            List[Item]: return result

        Raises:
            ApiNotEnabled: api is not invalid
        """
        params = {
            "key": self.token,
            "cx": self.engine_id,
            "q": keyword
        }
        res = requests.get(self.APIURL, params=params)
        return self._from_dict(res.json())

    def _from_dict(self, data: dict) -> List[Item]:
        "This is used to convert the json data to Item."
        if data.get('error'):
            raise ApiNotEnabled(
                data['error']['code'], data['error']['message'])
        else:
            return [Item(i) for i in data["items"]]

    async def search_async_iterator(self, *args, **kwargs) -> AsyncIterator[Item]:
        """It's like search_async, but this is iterator

        Args:
            keyword  (str): Search Word

        Yields:
            Item: Return result

        Note:
            You need aiohttp library.
        """
        for item in (await self.search_async(*args, **kwargs)):
            yield item

    async def search_async(self, q: str, *, safe: bool = False,
                           filter: bool = True) -> List[Item]:
        """This is an asynchronous version of custom_search.search.

        Args:
            q (str): Search word
            safe (bool): Safe search mode

        Returns:
            List[Item]: return result

        Raises:
            ApiNotEnabled: api is not invalid
            AsyncError: If you don't install aiohttp, lib call error.

        Note:
            You need aiohttp library.
        """
        if no_async:
            raise AsyncError(
                "This library can't use aiohttp. Please install aiohttp")
        payload = {
            "key": self.token,
            "cx": self.engine_id,
            "q": q
        }
        if safe:
            payload["safe"] = "active"
        if not filter:
            payload["filter"] = 0
        async with aiohttp.ClientSession() as session:
            async with session.get(self.APIURL, params=payload) as res:
                return self._from_dict(await res.json())
