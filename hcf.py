def hcf(x,y):
    a,b = 2,2;ans=1;
    arr1 = [];arr2 = []
    while(x>1):
        if(x%a == 0):
            arr1.append(a)
            x = x//a
        else:
            a+=1
    while(y>1):
        if(y%b == 0):
            arr2.append(b)
            y = y//b
        else:
            b+=1
        
    print("arr1:",arr1,"\narr2:",arr2,)
    l1 = len(arr1);l2 = len(arr2)
    for i in range(l1):
        for j in range(l2):
            if(arr1[i] == arr2[j]):
                ans = ans*arr1[i]
                break
    return ans            


if __name__=='__main__':
    n,k = map(int,input().split())
    result=hcf(n,k)
    print (result)
