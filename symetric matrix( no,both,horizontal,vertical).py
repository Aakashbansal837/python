for _ in range(int(input())):
    n = int(input())
    a=[];c1,c2=1,1
    for j in range(n):
        num = list(input())
        a.append(num)
    for i in range(n):
        for j in range(n//2):
            if a[i][j] != a[i][n-j-1]:
                c1=0
                break
        if c1 == 0:
            break
    for i in range(n//2):
        if a[i] != a[n-i-1]:
            c2=0
            break
    r = c1+c2
    if r == 0:
        print("NO")
    elif r==2:
        print("BOTH")
    else:
        if c1 == 1:
            print("VERTICAL")
        elif c2 == 1:
            print("HORIZONTAL")
        
