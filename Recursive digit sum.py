def sum(n):
    if(n <10):
        return n
    else:
        m=n
        while(n > 10):
            num = n%10
            n=n//10
        return num + sum(m//10)
    
if __name__ =="__main__":
    n,k = input().split()
    l = len(n);s=0;flag=1;
    n,k = [int(n),int(k)]
    for i in range(k):
        s = s*(10**l)
        s+=n
        print("s:",s)

    while(flag == 1):
        if (s<10):
            flag =0
        else:
            print("sum",s)
            s = sum(s)
print(s)
        
