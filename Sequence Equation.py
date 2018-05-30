n = int(input())
arr=[]
ar = [int(x) for x in input().split()]
ar.insert(0,0)
for i in range(1,n+1):
    arr.append(ar.index(ar[ar.index(ar.index(i))]))
print(*arr,sep="\n")
