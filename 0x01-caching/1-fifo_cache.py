#!/usr/bin/env python3
"""
TASK 1
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put
        """

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        get
        """
        return self.cache_data.get(key, None)
