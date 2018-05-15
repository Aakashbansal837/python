from itertools import *
n=int(input())
arr = input().split()
k=int(input())

lst = list(combinations(arr,k))
f = [i for i in lst if 'a' in i]
print("{:.4f}".format(len(f)/len(lst)))
    
