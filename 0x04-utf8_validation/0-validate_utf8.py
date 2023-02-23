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
    num_bytes = 0
    for num in data:
        to_binary = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for element in to_binary:
                if element == '0':
                    break
                num_bytes += 1
            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (to_binary[0] == '1' and to_binary[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
