for _ in range(int(input())):
    n,k = map(int,input().split())
    arr=[int(x) for x in input().split()]
    count = 0
    for i in arr:
        if i<= 0 :
            count+=1
    if count>=k:
        print("NO")
    else:
        print("YES")
