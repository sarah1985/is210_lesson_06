#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 03: Sorting Data """

import data


def bubble_sort(list_input):

    swapped = False
    first_run = True

    while first_run or swapped:

        swapped = False
        first_run = False

        for i in range(1, len(list_input)):

            if list_input[i - 1] > list_input[i]:

                a = list_input[i - 1]
                list_input[i-1] = list_input[i]
                list_input[i] = a
                swapped = True

    return list_input


#a = [5, 1, 9, 8, 6, 3, 0]
#sprint bubble_sort(a)