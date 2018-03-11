def cost(ch):
    flag = 1
    while(flag == 1):
        if(ch >100):
            ch=ch%100
        else:
            flag = 0
    while (ch > 20):
        if(ch < 100 and ch > 50):
            ch=100-ch
        elif (ch < 50 and ch > 20):
            ch=50-ch
        elif (ch >20):
            ch=20-ch
    if (ch > 9):
        return -1
    else:
        return ch
    
t = int(input())
for i in range(t):
    c,p = map(int,input().split())
    change = p-c
    if (change == 20 or change == 50 or change == 100 or change == 200 or change == 500 or change == 1000):
        print(0);continue
    else:
        result = cost(change)
        print(result)
