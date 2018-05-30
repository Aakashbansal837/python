def  pagesTurned(n,m):
    count = 0
    while(m>n):
        count+=1
        n+=2
    return count

n = int(input())
p = int(input())
num = 0
if p<=n//2:
    num = pagesTurned(1,p)
else:
    num = pagesTurned(p,n)
print(num)
