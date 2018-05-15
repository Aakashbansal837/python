for _ in range(int(input())):
    a=[]
    n,m = map(int,input().split())
    for i in range(m):
        num = list(map(int,input().split()))
        a.append(num)
    print(a)
