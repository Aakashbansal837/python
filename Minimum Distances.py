n = int(input())
arr = [int(x) for x in input().split()]
dist = 100000
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            num = j-i
            if num < dist:
                dist = num
if dist == 100000:
    print(-1)
else:
    print(dist)
