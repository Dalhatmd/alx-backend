#!/usr/bin/env python3
""" FIFO cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache implementation"""
    def put(self, key, item):
        """ inserts new item to dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

    def get(self, key):
        """ gets an item from the dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
