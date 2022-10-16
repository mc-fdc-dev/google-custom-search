import requests
try:
    from aiohttp import ClientSession
except ImportError:
    no_async = True
else:
    no_async = False

from typing import List
from .errors import ApiNotEnabled, AsyncError
from .types import Item


class CustomSearch:
    """This is the class used when using Google Custom Search.

    Args:
        apikey (str): Insert google custom search api key.
        engine_id (str): Insert google custom search engine id.
        aiohttp_options (dict): Custom aiohttp option.
    """
    APIURL: str = "https://www.googleapis.com/customsearch/v1"

    def __init__(
        self, apikey: str, engine_id: str,
        aiohttp_options: dict
    ):
        self.apikey = apikey
        self.engine_id = engine_id
        if not no_async:
            self.session = ClientSession(**aiohttp_options)
        else:
            self.session = None

    def _payload_maker(
        self, q: str, *,
        safe: bool = False,
        filter: bool = False
    ) -> dict:
        """Make payload

        Args:
            q (str): Search keyword
            safe (bool): Using safe mode
            filter (filter): Use filter mode

        Returns:
            dict: Return payload"""
        payload = {
            "key": self.apikey,
            "cx": self.engine_id,
            "q": q
        }
        if safe:
            payload["safe"] = "active"
        if not filter:
            payload["filter"] = 0
        return payload

    def search(self, *args, **kwargs) -> List[Item]:
        """This is searched using api.

        Args:
            q (str): Search keyword
            safe (bool): Using safe mode
            filter (filter): Use filter mode

        Returns:
            List[Item]: return result

        Raises:
            ApiNotEnabled: api is not invalid
        """
        res = requests.get(
            self.APIURL, params=self._payload_maker(*args, **kwargs))
        return self._from_dict(res.json())

    def _from_dict(self, data: dict) -> List[Item]:
        "This is used to convert the json data to Item."
        if data.get('error'):
            raise ApiNotEnabled(
                data['error']['code'], data['error']['message'])
        else:
            return [Item(i) for i in data["items"]]

    async def search_async(self, *args, **kwargs) -> List[Item]:
        """This is an asynchronous version of custom_search.search.

        Args:
            q (str): Search keyword
            safe (bool): Using safe mode
            filter (filter): Use filter mode

        Returns:
            List[Item]: return result

        Raises:
            ApiNotEnabled: api is not invalid
            AsyncError: If you don't install aiohttp, lib call error.

        Note:
            This function use aiohttp, so please install aiohttp.
        """
        if no_async:
            raise AsyncError(
                "This function use aiohttp, so please install aiohttp.")
        async with self.session.get(self.APIURL, params=self._payload_maker(*args, **kwargs)) as res:
            return self._from_dict(await res.json())
