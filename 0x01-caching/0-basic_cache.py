#!/usr/bin/env python3
""" caching system """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache with put and get methods """
    def put(self, key, item):
        """ adds an entry to dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ returns key from dictionary """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
