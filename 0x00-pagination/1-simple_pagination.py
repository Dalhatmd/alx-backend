#!/usr/bin/env python3
""" helper function """
import csv
import math
from typing import List


def index_range(page, page_size):
    """computes index range """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    index = (start_index, end_index)
    return index

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """computes page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        index = index_range(page, page_size)
        start, end = index
        data = self.dataset()
        return data[start:end]