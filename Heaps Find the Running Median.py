arr=[]
count=-1
for i in range(int(input())):
    arr.append(int(input()))
    count+=1
    arr.sort()
    num = count//2
    if count%2 != 0:
        print((arr[num]+arr[num+1])/2)
    else:
        print(float(arr[num]))
    
