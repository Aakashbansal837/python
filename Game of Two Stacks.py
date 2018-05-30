def find():
    n,m,val = map(int,input().split())
    arr = [int(x) for x in input().split()]
    brr = [int(x) for x in input().split()]
    s = 0
    count = 0
    tmp,tmp1 = 0,0
    while(s < val and n!=0 and m!=0):
        if arr[0] <= brr[0]:
            n-=1
            s+=arr[0]
            tmp=arr[0]
            tmp1 = 0
            arr=arr[1:]
            count+=1
        else:
            m-=1
            s+=brr[0]
            tmp = brr[0]
            tmp1 = 1
            brr=brr[1:]
            count+=1
    count-=1
    if tmp1 == 0:
        arr = [tmp]+arr
    else:
        brr = [tmp]+brr
    while(n > 0 and s<val):
        s+=arr[0]
        arr=arr[1:]
        count+=1
        n-=1
    while(m>0 and s<val):
            m-=1
            s+=brr[0]
            brr=brr[1:]
            count+=1
    print(count)

for i in range(int(input())):
    find()
