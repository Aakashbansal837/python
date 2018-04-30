n,m = map(int,input().split())
emp=[(i+1) for i in range(n)]
f=[0]*m
grp=[]
for i in range(m):
    k,f[i] = map(int,input().split())
    tmp2 = [int(x) for x in input().split()]
    grp.append(tmp2)
print("grp:",grp)
print("f:",f)
for i in range((n*2)-1):
    print("gp1:",[emp[:i+1]],"gp2:",emp[i+1:])
