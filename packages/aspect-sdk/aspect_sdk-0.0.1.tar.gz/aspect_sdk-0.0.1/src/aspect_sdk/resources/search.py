# Search resource - handles all search-related operations
from typing import Any
from aspect_sdk._generated import (
    SearchApi,
    Configuration,
    ApiClient,
)


class Search:
    """Search resource class for handling search operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = SearchApi(api_client)
    
    def query(self, search_data: Any) -> Any:
        """
        Search across indexed content
        
        Args:
            search_data: The search query data
            
        Returns:
            Search results
        """
        # The generated API currently has no payload defined. When search payload is
        # added to the OpenAPI spec, this wrapper can forward it.
        return self._api.post_search_search()
