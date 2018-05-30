a=[0]*101
n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    a[i]+=1
maxx = 0
for i in range(0,n-2):
    num = a[i]+a[i+1]
    if num  > maxx:
        maxx = num
print(maxx)
