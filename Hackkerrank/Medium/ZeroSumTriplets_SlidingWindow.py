#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findZeroSumTripletsInWindow' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY readings
#  2. INTEGER windowSize
#

def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    if len(readings) < windowSize:
        return []
    res = set()
    for i in range(len(readings) - windowSize + 1):
        window = readings[i:i + windowSize]
        window.sort()
        for j in range(len(window) - 2):
            if j > 0 and window[j] == window[j - 1]:
                continue
            left = j + 1
            right = len(window) - 1
            while left < right:
                total = window[j] + window[left] + window[right]
                if total == 0:
                    res.add((window[j], window[left], window[right]))

                    while left < right and window[left] == window[left + 1]:
                        left += 1
                    while left < right and window[right] == window[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
    return [list(x) for x in res]


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    windowSize = int(input().strip())

    result = findZeroSumTripletsInWindow(readings, windowSize)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
