def BigSort(arr, n):
    arr.sort(key = lambda x: (len(x), x))
arr=[]
for i in range(int(input())):
    arr.append(input())
    n = len(arr)
BigSort(arr, n)
for i in arr:
    print(i)
