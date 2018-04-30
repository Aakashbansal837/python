def solve():
    n = int(input())
    a = [0]*100
    b = list(map(int,input().split()))
    for i in b:
        a[i]+=1
    print(*a)

solve()
