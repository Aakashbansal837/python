n=int(input())
arr=0
for i in range(n):
    a,b=input().split()
    b=int(b)
    if a == "add":
        if b > 0:
            arr+=b
    elif a == "set":
        if b > arr:
            arr= b
print(arr)
