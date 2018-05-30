for i in range(int(input())):
    a,b,c = map(int,input().split())
    count = 0;num = 0
    for j in range(a,b+1):
        if j%c == 0:
            num = j
            break
    #print("num = ",num,"count = ",count)
    if num != 0:
        while(num <= b):
            #print("num in loop:",num)
            num = num+c
            count+=1
    print(count)
