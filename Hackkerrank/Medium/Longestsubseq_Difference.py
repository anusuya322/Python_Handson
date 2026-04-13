#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    # Write your code here
    if not arr:
        return 0
    arr=sorted(set(arr))
    di={}
    count=0
    for num in arr:
        if num not in di:
            di[num]=di.get(num-k,0)+1
            count=max(count,di[num])
    return count

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
