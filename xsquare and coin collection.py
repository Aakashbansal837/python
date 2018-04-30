s=0;prev = 0
for _ in range(int(input())):
    n,k = map(int,input().split(" "))
    a=[int(x) for x in input().split()]
    for i in range(n):
        if a[i] > k:
            if prev <=s:
                prev = s
            s=0
        elif a[i] <=k:
            s+=a[i]
    if s > prev:
        prev = s
    print(prev)
    s=0;prev=0
