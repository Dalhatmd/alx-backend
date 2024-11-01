#!/usr/bin/env python3
""" LRU cache """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache """
    def __init__(self):
        """ initialises using an OrderedDict"""
        super().__init__()
        self.cache_data = OrderedDict()

    """ LRU cache implementation """
    def get(self, key):
        """ gets an item from cache """
        if key is None or key not in self.cache_data:
            return

        # move the last gotten item to the end
        self.cache_data.move_to_end(key)

        return self.cache_data[key]

    def put(self, key, item):
        """ adds an item to cache """
        if key is None or item is None:
            return None

        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            least_item = self.cache_data.popitem(last=False)
            print(f"DISCARD {least_item[0]}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
