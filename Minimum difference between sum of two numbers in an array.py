for _ in range(int(input())):
    minn = 2*100000
    maxx = 1
    a=[int(x) for x in input().split()]
    num=a[0]
    a=a[1:]
    a=sorted(a)
    for i in range(num//2):
        num1 = a[i]+a[num-i-1]
        if num1 < minn:
            minn = num1
        if num1 > maxx:
            maxx = num1
    print(maxx-minn)
          #  print("min:",minn,"num:",num)
    #print(minn)
