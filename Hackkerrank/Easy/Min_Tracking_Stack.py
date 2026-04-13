#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    # Write your code here
    st=[]
    min_st=[]
    res=[]
    #minimum=st[-1]
    for ch in operations:
        op=ch.split()
        if op[0]=="push":
            val=int(op[1])
            st.append(val)
            if not min_st or val<=min_st[-1]:
                min_st.append(val)
        elif op[0]=="pop":
            if st:
                if st[-1]==min_st[-1]:
                    min_st.pop()
            st.pop()
        elif op[0]=="top":
            if st:
                res.append(st[-1])
        else:
            if min_st:
                res.append(min_st[-1])
    return res

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
