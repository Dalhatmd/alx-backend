#!/usr/bin/env python3
""" helper function """


def index_range(page, page_size):
    """computes index range """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    index = (start_index, end_index)
    return index
