from itertools import product
def square(lt):
    return list(map(lambda x: x ** 2, lt))

n,m = map(int,input().split())
l = [];ans=[]
for i in range (n):
    sl=[]
    sl = list(map(int,input().split()))
    sl.remove(sl[0])
    l.append(square(sl))
for e in product(*l):
    ans.append(sum(e)%m)
print(max(ans))
