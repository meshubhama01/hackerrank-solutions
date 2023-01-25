#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    diff = []
    new_brr = brr
    
    for i in list(set(brr)):
        if i not in list(set(arr)):
            diff.append(i)
            new_brr.remove(i)
    
    
    arr_count = Counter(arr)
    brr_count = Counter(new_brr)

    for i in list(set(arr)):
        if brr_count[i] > arr_count[i]:
            diff.append(i)
        
    diff.sort()
    return diff

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
