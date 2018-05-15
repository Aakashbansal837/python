for _ in range(int(input())):
    n,m,q = map(int,input().split())
    arr = [[0 for x in range(m)] for y in range(n)]
    arr1=[]
    for i in range(q):
        tmp,tmp2 = map(int,input().split())
        arr1.append([tmp-1,tmp2-1])
        arr[tmp-1][tmp2-1] = 1
    #print("array is:")
    #print(*arr,sep="\n")
    count = 0
    for i in arr1:
        #print("i:",i)
        x,y = i[0],i[1]
        if x-2 >= 0:
            if y-1 >= 0:
                if arr[x-2][y-1] == 1:
                    count+=1
                    #print("x-2:y-1")
            if y+1 < m:
                if arr[x-2][y+1] == 1:
                    count+=1
                    #print("x-2:y+1")
        if x+2 < n:
            if y-1 >= 0:
                if arr[x+2][y-1] == 1:
                    count+=1
                    #print("x+2:y-1")
            if y+1 < m:
                if arr[x+2][y+1] == 1:
                    count+=1
                    #print("x+2:y+1")
        if y-2 >= 0:
            if x-1 >= 0:
                if arr[x-1][y-2] == 1:
                    count+=1
                    #print("x-1:y-2")
            if x+1 < m:
                if arr[x+1][y-2] == 1:
                    count+=1
                    #print("x+1:y-2")
        if y+2 < m:
            if x-1 >= 0:
                if arr[x-1][y+2] == 1:
                    count+=1
                    #print("x-1:y-2")
            if x+1 < m:
                if arr[x+1][y+2] == 1:
                    count+=1
                    #print("x+1:y+2")
    print(count)
    
        
