#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 01: Even and Odds Function """


def evens_and_odds(numbers, show_even=True):
    """even list and odd list"""

    new_list = []

    for val in numbers:
        if val % 2 == 0 and show_even:
            new_list.append(val)

        elif val % 2 != 0 and not show_even:
            new_list.append(val)

    return new_list