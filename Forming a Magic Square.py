arr=[]
for i in range(3):
    arr.append(list(map(int,input().split())))
total = sum(arr[0])
r = 0
num = arr[0][0]+arr[1][0]+arr[2][0]
if num > total:
    r = num-total
    total = num
    
