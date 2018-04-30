import math
l=int(input())
for i in range(l):
    n,m=map(int, input().split())
    a=pow(2,n+1)
    b=pow(2,m+1)
    c=str(a-b)+".00"
    print(c)
 
