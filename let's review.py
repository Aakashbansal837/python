for _ in range(int(input())):
    a =list(input())
    odd,even =[],[]
    l = len(a)
    for i in range(l):
        if i%2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    print(*even,sep="",end=" ");print(*odd,sep="",end="\n")
               
