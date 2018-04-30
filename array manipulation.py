n, inputs = [int(x) for x in input().split()]
l = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split()]
    l[x-1] += incr
    print("After x:",l)
    if((y)<=len(l)):
        l[y] -= incr;
    print("after y:",l)
maxx = x = 0
for i in l:
   x=x+i;
   if(maxx<x): maxx=x;
print(maxx)
