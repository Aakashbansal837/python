from itertools import *
n=int(input())
arr = input().split()
k=int(input())

lst = list(combinations(arr,k))
print(lst)
f = [i for i in lst if 'a' in i]
print(f)
print("{:.4f}".format(len(f)/len(lst)))
    
