from bisect import bisect_left as bl
import sys
 
q=int(sys.stdin.readline())
m=[]
s=[0]
for i in  range(q):
    x,y,z=map(int,sys.stdin.readline().split())
    # print(m)
    if x==1:
        m.append([z,y])
        s.append(s[-1]+y)
    else:
        a=bl(m,[z,0])
        b=bl(m,[z-y,0])
        su=0
        sys.stdout.write(str(s[a]-s[b])+"\n")
