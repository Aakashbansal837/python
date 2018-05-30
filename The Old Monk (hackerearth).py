def M(arr,brr,n):
    maxx = 0
    for i in range(n):
        for j in range(i,n):
            if brr[j] >= arr[i]:
                num =j-i
                if num > maxx:
                    maxx = num
            elif brr[j] < arr[i]:
                break
    return maxx

for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    print(M(arr,brr,n))
