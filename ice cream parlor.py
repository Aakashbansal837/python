def solve():
    for _ in range(int(input())):
        m = int(input())
        n = int(input())
        a = list(map(int,input().split()))
        for i in range(n):
            num1 = a[i]
            for j in range(i+1,n):
                num2 = a[j]
                if (num1+num2) == m:
                    print(i+1,j+1,sep=" ")
                    break
            if (num1+num2) == m:
                    break
            

solve()
