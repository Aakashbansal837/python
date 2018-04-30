n,m = map(int,input().split())
lastanswer=0
s0=[];s1=[]
for i in range(m):
    a,b,c = map(int,input().split())
    num = ((b^lastanswer)%n)
    if a == 1:
        if num == 0:
            s0.append(c)
        elif num == 1:
            s1.append(c)
    if a == 2:
        if num == 0:
            lastanswer = s0.pop()s
            s0.append(lastanswer)
        elif num == 1:
            lastanswer = s1.pop()
            s1.append(lastanswer)
            print(lastanswer)
