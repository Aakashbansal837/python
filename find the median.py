n=int(input())
ar = list(map(int,input().split()))
ar=sorted(ar)
mid = (n+1)//2 - 1
print(ar[mid])
