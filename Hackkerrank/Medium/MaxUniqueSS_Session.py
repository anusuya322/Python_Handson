#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    # Write your code here
    if len(sessionString)<1 or (len(sessionString)==1 and sessionString=='*'):
        return 0
    session=sessionString.split('*')
    maxLen=0
    for s in session:
        lt=0
        unique_ele=set()
        for rt in range(len(s)):
            while s[rt] in unique_ele:
                unique_ele.remove(s[lt])
                lt+=1
            unique_ele.add(s[rt])
            maxLen=max(maxLen,rt-lt+1)
    return maxLen

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
