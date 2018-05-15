arr=[[]for x in range(6)]
for i in range(int(input())):
    n,m  = map(int,input().split())
    for j in range(m):
        arr[i].append([x for x in input().split()])
print(*arr,sep="\n\n")
