def savetheprisoner():
    n,m,s = map(int,input().split())
    a = s+m-1
    if a > n:
        if a%n == 0:
            return n
        return a%n
    return a

for i in range(int(input())):
    print(savetheprisoner())
