n= int(input().strip())
a = list(map(int,input().split()))
maxx = a[0];index=0
while(len(a) >0):
    for i in range(len(a)):
        if(a[i] > maxx):
            maxx = a[i]
    for i in range(len(a)):
        if a[i] == maxx:
            index=i
            break
    if a[0] == maxx:
        break
    else:
        a = a[:index]
    print(*a)
    
