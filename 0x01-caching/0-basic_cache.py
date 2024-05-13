#!/usr/bin/env python3
"""
TASK 0
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system:
    """

    def put(self, key, item):
        """
        put
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get
        """

        return self.cache_data.get(key, None)
