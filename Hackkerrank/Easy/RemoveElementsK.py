#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    # Write your code here
    if len(timestamps)==0:
        return 0
    i=1
    last=timestamps[0]
    while i<len(timestamps):
        if timestamps[i]-last>=K:
            last=timestamps[i]
            i+=1
        else:
            del timestamps[i]
    return len(timestamps)

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
