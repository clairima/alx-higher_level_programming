#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    cen = size
    cen2 = size // 2

    if size == 0:
        return None

    while True:
        cen = cen // 2
        if (cen2 < size - 1 and
                list_of_integers[cen2] < list_of_integers[cen2 + 1]):
            if cen // 2 == 0:
                cen = 2
            cen2 = cen2 + cen // 2
        elif cen > 0 and list_of_integers[cen2] < list_of_integers[cen2 - 1]:
            if cen // 2 == 0:
                cen = 2
            cen2 = cen2 - cen // 2
        else:
            return list_of_integers[cen2]
