k,m=map(int,input().split())
arr=[0]*(k)
max_num = 0
for i in range(m):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        arr[j] += c
    max_num +=c
    print("arr:",arr)
result = (max(arr))*max_num;
print(result)
