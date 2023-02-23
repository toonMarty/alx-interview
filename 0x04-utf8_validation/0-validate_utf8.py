#!/usr/bin/python3
"""
This module contains a method that determines if
a given set of data is a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    This method determines if a given set of data
    is a valid UTF-8 encoding
    Args:
        data (list): a data set of integers
    Return:
         True if data is a valid utf-8 encoding
            else
        False if data set is not a valid utf-8 encoding
    """
    if max(data) > 127:
        return False
    return True
