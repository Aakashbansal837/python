#!/bin/python3

import os
import sys

def f(a, m, k):
    ans = 0
    f = {1: 1}
    p = 1
    for x in a:
        p = p * x % m
        ans += f.get(p * pow(k, m - 2, m) % m, 0)
        f[p] = f.get(p, 0) + 1
    
    return ans

def howManyGoodSubarrays(A, m, k):
    a = []
    ans = 0
    y = 0
    for x in A:
        if x % m != 0:
            a += [x]
        else:
            ans += f(a, m, k)
            y += len(a) * (len(a) + 1) // 2
            a = []
    
    ans += f(a, m, k)
    y += len(a) * (len(a) + 1) // 2
    
    if k == 0: ans = len(A) * (len(A) + 1) // 2 - y
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nmk = input().split()

        n = int(nmk[0])

        m = int(nmk[1])

        k = int(nmk[2])

        A = list(map(int, input().rstrip().split()))

        result = howManyGoodSubarrays(A, m, k)

        fptr.write(str(result) + '\n')

    fptr.close()
