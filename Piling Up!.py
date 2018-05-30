def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    num,num2 = arr[0],arr[n-1]
    num3 = max(arr)
    if num == num3 or num3 == num2:
        print("Yes")
    else:
        print("No")


for i in range(int(input())):
    solve()
