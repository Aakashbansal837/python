def factorial(n):
    if n <= 1:
        return 1
    else:
        num = 1
        while n >1:
            num = num *n
            n-=1
        return num
for i in range(int(input())):
    n = int(input())
    num = 3*factorial(n)+3
    print(num%1000000007)
