#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 03: Sorting Data """

import data


def bubble_sort(list_input):
    """bubble sort a list"""

    swapped = False
    first_run = True

    while first_run or swapped:

        swapped = False
        first_run = False

        for i in range(1, len(list_input)):

            if list_input[i - 1] > list_input[i]:

                temp = list_input[i - 1]
                list_input[i-1] = list_input[i]
                list_input[i] = temp
                swapped = True

    return list_input

SORT = bubble_sort(data.TASK_O1)
print SORT