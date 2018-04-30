for _ in range(int(input())):
    n,m =map(int,input().split())
    a=[[0 for x in range(n)] for y in range(n)]
    for i in range(m):
        x,y,w=map(int,input().split())
        a[x-1][y-1]=w
    start=int(input())-1
    for i in range(n):
    
            
