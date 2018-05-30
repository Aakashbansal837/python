#---------finding gcd here-----------------
def findgcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
#---------finding lcm here------------------
def findlcm(a,b):
    return a*b/findgcd(a,b)
#-----creating array of all gcd-------------
def gcd(arr,n):
    a = []
    for i in range(n-1):
        a.append(findgcd(arr[i],arr[i+1]))
    return a
#----creating array of all lcm--------------
def lcm(arr,n):
    a=[]
    for i in range(n-1):
        a.append(findlcm(arr[i],arr[i+1]))
    return a
#--------driver code------------------------
n,m = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
brr = gcd(brr,m)
arr = lcm(arr,n)
