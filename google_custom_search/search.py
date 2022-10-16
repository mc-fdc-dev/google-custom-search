# google-custom-seaerch - search

from typing import List

from .types import Item
from .adapter import BaseAdapter


class CustomSearch:
    """This is the class used when using Google Custom Search.

    Args:
        apikey (str): Insert google custom search api key.
        engine_id (str): Insert google custom search engine id.
        aiohttp_options (dict): Custom aiohttp option.
    """
    APIURL: str = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter

    def search(self, *args, **kwargs) -> List[Item]:
        """This is searched using api.

        Args:
            query (str): Search keyword
            safe (bool): Using safe mode
            filter_ (filter): Use filter mode

        Returns:
            List[Item]: return result

        Raises:
            ApiNotEnabled: api is not invalid
        """
        return self.adapter.search(*args, **kwargs)
