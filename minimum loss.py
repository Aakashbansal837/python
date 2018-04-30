def solve():
    n = int(input());min_loss = 10**16
    a = list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            num = (a[i]-a[j])
            if (num < 0):
                continue
            if num < min_loss:
                min_loss = num
    print(min_loss)

solve()
