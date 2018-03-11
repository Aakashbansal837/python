m = ""
while(m !="."):
    m = input("enter m:")
    if(m == "."):
        break
    a= list(map(int,input().split()))
    m = int(m)
    sum =0
    for i in range(len(a)):
        sum+=(pow(a[i],2))
    result = sum%m
    print(result)


'''
10 867
2 5 3
3 22 34 67
3 11 88 45
4 99 98 97 87
4 85 54 45 65
5 1 2 3 4 5
5 4 4 4 4 4
6 7 7 8 8 9 2
5 11 23 56 34 45
5 44 55 33 22 77
'''
