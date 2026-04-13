#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    '''for i in range(0,len(taskDurations)):
        for j in range(i+1,len(taskDurations)):
            if(taskDurations[i]+taskDurations[j]==slotLength):
                return [i,j]
    return [-1,-1]'''
    seen={}
    for i in range(len(taskDurations)):
        comp=slotLength-taskDurations[i]
        if comp in seen:
            return seen[comp],i
        seen[taskDurations[i]]=i
    return [-1,-1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
`