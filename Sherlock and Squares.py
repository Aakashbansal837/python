from math import *
for i in range(int(input())):
    n,m = map(int,input().split())
    print(floor(sqrt(m)-ceil(sqrt(n))+1))
