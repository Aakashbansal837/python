def insertionsort(a,m):
    count=0
    for i in range(m):
        if a == sorted(a):
            break
        while(i>0):
            if a[i] < a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                count+=1;i-=1
            else:
                break
    print(count)


    
def solve():
    for _ in range(int(input())):
        m = int(input())
        a = list(map(int,input().split()))
        if a == sorted(a):
            print("0")
        else:
            insertionsort(a,m)
        

solve()
