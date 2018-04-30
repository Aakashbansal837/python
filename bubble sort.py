def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    num_swaps=0
    for i in range(0,n-1):
        for j in range(1,n):
            if (a[j] < a[j-1]):
                a[j],a[j-1]=a[j-1],a[j]
                num_swaps+=1
    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element:",a[0])
    print("Last Element:",a[n-1])

solve()
