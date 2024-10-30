#!/usr/bin/env python3
""" MRU Cache """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """ gets an item from cache"""
        if key is None or key not in self.cache_data:
            return
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

    def put(self, key, item):
        if key is None or item is None:
            return None
        
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            most_used = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_used[0]}")