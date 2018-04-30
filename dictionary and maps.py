a,b=[],[]
t=int(input())
for i in range(t):
    m,n=input().split()
    a.append([m,n])
    b.append(m)
while(True):
    num=input()
    if (num.strip() == ""):
        break
    else:
        if num in b:
            l=b.index(num)
            print(a[l][0],"=",a[l][1],sep="")
        else:
            print("Not found")
