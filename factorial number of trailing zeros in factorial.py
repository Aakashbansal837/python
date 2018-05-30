import sys
sys.setrecursionlimit(10000)

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

num = list((str(factorial(int(input())))))
l = len(num)-1
count = 0
while l:
    if num[l] == '0':
        count+=1
    else:
        break
    l-=1
print(count)
