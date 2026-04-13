#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def getAutoSaveInterval(n):
    # Write your code here
    if n==0:
        return 1
    if n==1:
        return 2
    a,b=1,2
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)

