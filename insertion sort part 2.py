def solve():
    n = int(input())
    a =list(map(int,input().split()))
    for i in range(1,n):
        while(i>0):
            if (a[i] < a[i-1]):
                a[i],a[i-1] = a[i-1],a[i]
                i-=1
            else:
                break
        print(*a)    
            
solve()
