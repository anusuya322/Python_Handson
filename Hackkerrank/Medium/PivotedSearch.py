
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'searchRotatedTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def searchRotatedTimestamps(nums, target):
    # Write your code here
    if len(nums)==0:
        return -1
    start=0
    end=len(nums)-1
    while (start<=end):
        mid=(start+end)//2
        if(nums[mid]==target):
            return mid
        if nums[start]<=nums[mid]:
            if nums[start]<=target <nums[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if nums[mid]<target<=nums[end]:
                start=mid+1
            else:
                end=mid-1
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = searchRotatedTimestamps(nums, target)

    print(result)
