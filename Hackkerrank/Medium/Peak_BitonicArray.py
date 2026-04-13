#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findPeakIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY counts as parameter.
#

def findPeakIndex(counts):
    # Write your code here
    max_ele=counts[0]
    for i in range(1,len(counts)):
        max_ele=max(max_ele,counts[i])
    return counts.index(max_ele)

if __name__ == '__main__':
    counts_count = int(input().strip())

    counts = []

    for _ in range(counts_count):
        counts_item = int(input().strip())
        counts.append(counts_item)

    result = findPeakIndex(counts)

    print(result)
