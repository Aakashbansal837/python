n = int(input())
arr = list(map(int,input().split()))
while n != 0:
    print(n)
    brr = []
    num = min(arr)
    for i in range(0,n):
        arr[i]-=num
        if arr[i] != 0:
            brr.append(arr[i])
    arr = brr
    n = len(arr)
