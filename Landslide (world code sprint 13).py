#--road creation--------------
n = int(input())
road =[[0 for i in range(n+1)]for j in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    road[a][b] = 1
    road[b][a] = 1
print(*road,sep="\n")
#------query processing---------
for i in range(int(input())):
    c,a,b = input().split()
    if c == 'd':
        arr[a][b] = 2
    if c == 'c':
        if arr[a][b] == 2:
            arr[a][b] = 1
    if c == "q":
         



