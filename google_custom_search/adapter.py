# google-custom-search - adapter

from typing import Any, List

from abc import ABCMeta, abstractmethod

from requests import Session
try:
    from aiohttp import ClientSession
except ImportError:
    async_mode = False
else:
    async_mode = True

from .errors import AsyncError, ApiNotEnabled
from .types import Item


class BaseAdapter(metaclass=ABCMeta):
    """This is the base class for adapters.

    Args:
        apikey (str): Insert google custom search api key.
        engine_id (str): Insert google custom search engine id.

    Attributes:
        APIURL (str): Google Custom Search API URL
    """

    APIURL = "https://www.googleapis.com/customsearch/v1"
    session: Any = None

    def __init__(self, apikey: str, engine_id: str):
        self.apikey = apikey
        self.engine_id = engine_id

    @abstractmethod
    def request(self, method: str, path: str, *args, **kwargs) -> Any:
        ...

    @abstractmethod
    def search(self, *args, **kwargs) -> List[Item]:
        ...

    def _from_dict(self, data: dict) -> List[Item]:
        if data.get('error'):
            raise ApiNotEnabled(
                data['error']['code'], data['error']['message'])
        else:
            return [Item(i) for i in data["items"]]

    def _payload_maker(
        self, query: str, *,
        safe: bool = False,
        filter_: bool = False
    ) -> dict:
        payload = {
            "key": self.apikey,
            "cx": self.engine_id,
            "q": query
        }
        if safe:
            payload["safe"] = "active"
        if not filter_:
            payload["filter"] = 0
        return payload


class RequestsAdapter(BaseAdapter):
    "This class is requestsadapter for sync mode."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__session = Session()

    def request(self, method: str, path: str, *args, **kwargs) -> dict:
        return self.__session.request(
            method, self.APIURL + path, *args, **kwargs
        ).json()

    def search(self, *args, **kwargs) -> List[Item]:
        return self._from_dict(
            self.request(
                "GET", "/", params=self._payload_maker(*args, **kwargs)
            )
        )


class AiohttpAdapter(BaseAdapter):
    "This class is aiohttpadapter for async mode."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not async_mode:
            raise AsyncError(
                "This adapter use aiohttp, so please install aiohttp")
        self.__session = ClientSession(*args, **kwargs)

    async def request(self, method: str, path: str, *args, **kwargs) -> dict:
        async with self.__session.request(
            method, self.APIURL + path, *args, **kwargs
        ) as r:
            return await r.json()

    async def search(self, *args, **kwargs) -> List[Item]:
        r = await self.request(
            "GET", "/", params=self._payload_maker(*args, **kwargs)
        )
        return self._from_dict(await r.json())
