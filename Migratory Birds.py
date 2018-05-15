count=[0,0,0,0,0]

n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    count[i-1]+=1
print(count.index(max(count))+1)
