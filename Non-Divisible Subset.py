from itertools import combinations
n,k = map(int,input().split())
arr = [int(x) for x in input().split()]
arr=list(set(arr));n = len(arr)
for i in range(n):
    arr[i] = arr[i]%k
count = 0
for x in combinations(arr,2):
    num = x[0]+x[1]
    if num%k != 0:
        count+=1
print(count)
    

