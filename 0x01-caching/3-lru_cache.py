#!/usr/bin/env python3
""" LRU cache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache """
    def __init__(self):
        """ initialises using an OrderedDict"""
        super().__init__()
        self.used_keys = []

    """ LRU cache implementation """
    def get(self, key):
        """ gets an item from cache """
        if key is None or key not in self.cache_data:
            return
        self.used_keys.remove(key)
        self.used_keys.append(key)
        return self.cache_data[key]

    def put(self, key, item):
        """ adds an item to cache """
        if key is None or item is None:
            return None

        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            least_item = self.used_keys.pop(0)
            self.cache_data.pop(least_item)
            print(f"DISCARD {least_item[0]}")
        self.cache_data[key] = item
        self.used_keys.append(key)
