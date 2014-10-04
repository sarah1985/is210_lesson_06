#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 02: Average of a List """

import task_01
import data
import locale
locale.setlocale(locale.LC_ALL, '')


def get_average(numbers):
    """get average of list"""

    sum = 0

    for val in numbers:
        sum += val

    mean = float(sum)/len(numbers)

    return mean

TOTAL_AVG = get_average(data.TASK_O1)

EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))

ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, show_even=False))

REPORT = """

TASK 02 Report
--------------------------------
Total AVG:  {}
Even AVG:   {}
Odd AVG:    {}
""".format(locale.format('%.2f', TOTAL_AVG, True), locale.format('%.2f', EVEN_AVG, True), locale.format('%.2f', ODD_AVG, True))

print REPORT

