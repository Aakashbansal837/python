def solve():
    n,m = map(int,input().split())
    s=[[]for i in range(n)]
    lastanswer=0
    for i in range(m):
        a,b,c = map(int,input().split())
        num = ((b^lastanswer)%n)
        if a == 1:
            s[num].append(c)
        if a == 2:
            lastanswer = s[num][c%len(s[num])]
            print(lastanswer)

solve()
