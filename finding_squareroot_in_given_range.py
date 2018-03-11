m,n = map(int,input("enter Range:").split())
a=[]
a.append(m)
a.append(m+1)
avg = (m+n)//2
a.append(avg)
a.append(n-1)
a.append(n)

for i in range(5):
    result = pow(a[i],2)
    print("test case:",i+1,":power of ",a[i],"is:",result)

