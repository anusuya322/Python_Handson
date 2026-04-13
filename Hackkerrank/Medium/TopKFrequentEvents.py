#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    # Write your code here
    if k == 0 or not events:
        return []
    di={}
    res=[]
    first_index={}
    for i,e in enumerate(events):
        di[e]=di.get(e,0)+1
        if e not in first_index:
            first_index[e]=i
    sorted_di=sorted(di.items(),key=lambda x:(-x[1],first_index[x[0]]))
    return [sorted_di[i][0] for i in range(min(k,len(sorted_di)))]

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
