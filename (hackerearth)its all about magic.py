for _ in range(int(input())):
    num=1
    c1=1;c0=0
    m=int(input())
    for i in range(m):
        tmp=c1
        c1=c0
        c0+=tmp
    print(c1,c0)
