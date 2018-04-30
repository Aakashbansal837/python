n = int(input())
a = list(map(int,input().split()))
big = -1;bigp = -1;arr=[]
for i in range(0,n-2):
    for j in range(i+1,n):
        if a[j] not in arr:
            if a[i] == a[j]:
                print("matched",a[i])
                arr.append(a[i])
                break
    if j == n-1:
        big = a[j]
    if bigp < big:
        bigp = big
print(big)
print(bigp)
