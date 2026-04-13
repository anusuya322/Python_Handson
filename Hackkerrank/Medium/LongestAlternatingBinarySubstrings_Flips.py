#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestAlternatingSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def longestAlternatingSubstring(s, k):
    # Write your code here
    # if k==0:
    #return len(s)
    ans=0
    for start in [0,1]:
        left=0
        flips=0
        for right in range(len(s)):
            exp=str((right+start)%2)
            if s[right]!=exp:
                flips+=1
            while flips>k:
                exp_left=str((left+start)%2)
                if s[left]!=exp_left:
                    flips-=1
                left+=1
            ans=max(ans,right-left+1)
    return ans

if __name__ == '__main__':
    s = input()

    k = int(input().strip())

    result = longestAlternatingSubstring(s, k)

    print(result)
