n = int(input())
a=list(input().split())
if n == 0:
    print(0,0)
else:    
    
    minl,maxl = 0,0
    minl=len(a[0])
    for j in a:
        jj = list(j)
        l=len(jj)
        tmp,tmp1=0,0
        count=0
        for i in jj:
            if i == "w":
                tmp+=1
            elif i == "v":
                tmp1+=1
            else:
                count+=1
        if minl >= l:
            if tmp1%2 == 0:
                minl = tmp+tmp1//2+count
                #print("first")
            else:
                minl = tmp+tmp1//2+1+count
                #print("second")
        if maxl < l:
            maxl = tmp+tmp+tmp1+count
        #print(minl,maxl)
    print(minl,maxl)
    
