v=int(input())
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if(a[i] == v):
        print(i)
        break
