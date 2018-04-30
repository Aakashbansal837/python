def quicksort(a,n):
    pivot = a[0]
    l,r,e = [],[],[]
    for i in a:
        if pivot == i:
            e.append(i)
        if pivot > i:
            l.append(i)
        if pivot < i:
            r.append(i)
    print(*l,*e,*r)

def solve():
    n = int(input())
    a= list(map(int,input().split()))
    quicksort(a,n)


solve()
