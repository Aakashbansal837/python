arr1=[]
n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    if i in arr1:
        arr1.remove(i)
    else:
        arr1.append(i)
print(*arr1)
