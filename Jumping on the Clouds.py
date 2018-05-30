n = int(input())
arr = [int(x) for x in input().split()]
count = 0
i=0
while i < n-2:
    if arr[i+2] == 0:
        i+=2
        count+=1
    elif arr[i+1] == 0:
        i+=1
        count+=1
if i+2 == n:
    count+=1
print(count)
