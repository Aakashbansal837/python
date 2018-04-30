def solve():
    n1,n2,n3 = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = list(map(int,input().split()))
    for i in arr1:
        sum1+=i
    for i in arr2:
        sum2+=i
    for i in arr3:
        sum3+=i
    if(sum1 == sum2 and sum2 == sum3):
        print(sum1)
    

solve()
