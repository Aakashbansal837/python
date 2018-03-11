#!/bin/python3

import sys

def insertionSort1(n, arr):
    k =n-1;i =1
    e = arr[k]
    while (k >= 0):
        if (e < arr[k-1] and k !=0):
            arr[k] = arr[k-1]
            print(*arr)
            k-=1
        elif(k == 0):
            arr[k] = e
            print(*arr)
            k = -1
        else:
            arr[k] = e
            print(*arr)
            k = -1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
