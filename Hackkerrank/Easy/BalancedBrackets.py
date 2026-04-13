#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#


def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    st=[]
    di={']':'[',')':'(','}':'{'}
    for ch in code_snippet:
        if ch in '({[':
            st.append(ch)
        elif ch in ')}]':
            if not st or st[-1]!=di[ch]:
                return 0
            st.pop()
    if len(st)==0:
        return 1
    return 0

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
