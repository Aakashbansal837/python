n,rval,gval,bval=map(int,input().split())
r=[]
g=[]
b=[]
flag=0
flagg=0
flagb=0
temp=0
tempg=0
tempb=0

for i in range(n):
    for j in range(rval):
        r.append(flag)
        temp=temp+1
        if temp==rval:
            if flag == 0:
                flag=1
            elif flag==1:
                flag=0
            temp=0
    for j in range(gval):
        g.append(flagg)
        tempg=tempg+1
        if tempg==gval:
            if flagg == 0:
                flagg=1
            elif flagg==1:
                flagg=0
            tempg=0
    for j in range(bval):
        b.append(flagb)
        tempb=tempb+1
        if tempb==bval:
            if flagb == 0:
                flagb=1
            elif flagb==1:
                flagb=0
            tempb=0
    
ans=[]        
for i in range(n):
    if r[i]==1:
        if g[i]==0:
            if b[i]==0:
                ans.append("r")
            else:
                ans.append("m")
        else:
            if b[i]==0:
                ans.append("y")
            else:
                ans.append("w")
    else:
        if g[i]==0:
            if b[i]==0:
                ans.append("bla")
            else:
                ans.append("blu")
        else:
            if b[i]==0:
                ans.append("g")
            else:
                ans.append("c")
print(ans.count("r"),ans.count("g"),ans.count("blu"),ans.count("y"),ans.count("c"),ans.count("m"),ans.count("w"),ans.count("bla"))
                
        

