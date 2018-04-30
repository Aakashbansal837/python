def countingsort(a,n):
    for i in range(1,n):
        while(i>0):
            if (a[i][0] < a[i-1][0]):
                a[i],a[i-1] = a[i-1],a[i]
                i-=1
            else:
                break
    return a   
            
def solve():
    n = int(input())
    a=[]
    for i in range(n):
        num = input().split()
        num[0] = int(num[0])
        if i <= n//2-1:
            num[1] = "-"
        a.append(num)
    a = countingsort(a,n)
    for i,j in a:
        print(j,end=" ")
    

solve()
