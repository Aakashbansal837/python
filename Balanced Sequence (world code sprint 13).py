#!/bin/python3

import os

def fewestOperationsToBalance(s):
    t = []
    for c in s:
        if len(t) == 0 or t[-1] + c != '()': t += c
        else: del t[-1]
    
    a = t.count('(')
    b = t.count(')')
    
    return min(a, 1) + min(b, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = fewestOperationsToBalance(s)

    fptr.write(str(result) + '\n')

    fptr.close()
