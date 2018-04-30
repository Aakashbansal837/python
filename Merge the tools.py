st = input()
k = int(input())
n = len(st)
arr=[]
for i in range(0,n,k):
    arr.append(st[i:i+k])
for i in arr:
    arr1 = (((i)))
    print("".join(arr1))
print(arr)
