for _ in range(int(input())):
    c1,c2,m = map(int,input().split())
    d1 = abs(c1-m)
    d2 = abs(c2-m)
    if d1 == d2:
        print("Mouse C")
    elif d1 < d2:
        print("Cat A")
    elif d1 > d2:
        print("Cat B")
