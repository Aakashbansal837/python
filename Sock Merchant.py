def findpair(i):
    if i<=1:
        return 0
    else:
        count=0
        while(i >=2):
            i-=2
            count+=1
        return count

a = [0]*101
n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    a[i]+=1
count=0
for i in a:
    if i!= 0:
        count+=findpair(i)
print(count)
