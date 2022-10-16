# google-custom-search - adapter

from typing import Any

from requests import Session
try:
    from aiohttp import ClientSession
except ImportError:
    async_mode = False
else:
    async_mode = True

from .errors import AsyncError


class BaseAdapter:
    APIURL = "https://www.googleapis.com/customsearch/v1"
    session: Any = None

    def request(self, method: str, path: str, *args, **kwargs) -> Any:
        return self.session.request(
            method, self.APIURL + path, *args, **kwargs
        )


class RequestsAdapter(BaseAdapter):

    def __init__(self, *args, **kwargs):
        self.session = Session()


class AiohttpAdapter(BaseAdapter):

    def __init__(self, *args, **kwargs):
        if not async_mode:
            raise AsyncError(
                "This adapter use aiohttp, so please install aiohttp")
        self.session = ClientSession(*args, **kwargs)
