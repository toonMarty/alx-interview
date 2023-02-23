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
    res = []
    for element in data:
        to_binary = bin(element).lstrip('0b')
        res.append(to_binary)

    for bin_element in res:
        if len(bin_element) > 7:
            return False
        return True
