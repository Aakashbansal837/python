def solve():
    n = int(input());count=0
    a =list(map(int,input().split()))
    for i in range(1,n):
        while(i>0):
            if (a[i] < a[i-1]):
                a[i],a[i-1] = a[i-1],a[i]
                i-=1
                count+=1
            else:
                break
    print(count)    
            
solve()
