m = int(input())
for i in range(0,m):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    print("a=",a)
    b= [0]
    num = a[0]//k
    print("num=",num)
    b.append(num)
    for i in a:
        for j in range(1,len(b)):
            c =b[j]+b[j-1]
            if(c == i):
                break;
            else:
                nn = i-b[j]
                b.append(nn)
    print("a:",a)
    print("b:",b)
