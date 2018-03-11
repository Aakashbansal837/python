def solve():
    arr=[];max=-100;sum=0
    for _ in range(6):
        num = [int(temp) for temp in input().split()]
        arr.append(num)
    for i in range(4):
        for j in range(4):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if max < sum:
                max = sum
    print(max)
solve()
