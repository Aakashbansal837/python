#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if (v1 > v2):
        while(x1 < x2):
            x1+= v1  
            x2+= v2
        if (x1 == x2):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
