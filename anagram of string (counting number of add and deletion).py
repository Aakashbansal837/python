for _ in range(int(input())):
    a = list(input())
    b = list(input())
    count=0
    arr=[]
    for i in a:
        if i in b:
            b.remove(i)
        else:
            arr.append(i)
    print(len(b)+len(arr))
