#!/usr/bin/python3
""" MRU cache implementation """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache implementation"""

    def __init__(self):
        """initialiser"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put function"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop()
                self.cache_data.pop(removed)
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """get method"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
