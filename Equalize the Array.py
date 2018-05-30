a = [0]*101
n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    a[i]+=1
print(n-(max(a)))
