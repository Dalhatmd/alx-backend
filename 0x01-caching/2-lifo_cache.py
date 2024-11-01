#!/usr/bin/env python3
""" LIFO cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache implementation"""
    def put(self, key, item):
        """ adds an item to cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            # + 1 to check if it would be greater after adding
            last_item = self.cache_data.popitem()
            print(f"DISCARD: {last_item[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
