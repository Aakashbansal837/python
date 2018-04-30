for i in range(int(input())):
    a=[int(x) for x in input().split()]
    arr=[]
    for i in range(1,25):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            arr.append([chr(97+i),a[i]])
    print(arr)
    
