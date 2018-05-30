import sys
sys.setrecursionlimit(10000)

a =[0]*10000005
a[0] = 1
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        if a[n] == 0:
            a[n] = n*factorial(n-1)
        return a[n]

print(factorial(int(input())))
