n,m,q = map(int,input().split())
arr = [int(x) for x in input().split()]
for i in range(m):
    arr.insert(0,arr.pop())
for i in range(q):
    print(arr[int(input())])
