n = int(input())
arr = [int(x) for x in input().split()]
d,m = map(int,input().split())
count = 0
for i in range(0,n-m+1):
    tmp = 0
    for j in range(i,i+m):
        tmp +=arr[j]
    if tmp == d:
        count+=1
print(count)
