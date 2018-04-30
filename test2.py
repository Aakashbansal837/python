n=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
a.reverse()
c,pc=1,1
tmp=a[0]
for i in range(n):
    if a[i] == tmp:
        c+=1
    else:
        if c < pc:
            print("No")
            break
        else:
            pc = c
            c=0
            tmp=a[i]
if i == n-1:
    print("Yes")
    
    
    
