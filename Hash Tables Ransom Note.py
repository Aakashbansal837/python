m,n = map(int,input().split())
arr = [x for x in input().split()]
brr = [x for x in input().split()]
dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1
if n > m:
    print("No")
else:
    flag = 0
    for i in brr:
        if i in dict:
            if dict[i] == 0:
                flag = 1
                break
            dict[i] -=1
        else:
            flag = 1
            break
            
    if flag == 1:
        print("No")
    else:
        print("Yes")
