def solve():
    for _ in range(int(input())):
        n = int(input());flag = 0
        a = list(map(int,input().split()))
        for i in range(1,n-1):
            suml=sum(a[:i])
            sumr=sum(a[i+1:])
            if (suml == sumr):
                flag =1
                break
        if flag == 1:
            print("YES")
        else:
            print("NO")
            
solve()
