def show(array,m):
    n=len(array)
    temp=[]
    for i in range(n):
        temp.append(0)
    sq=0
    sqlist=[]
    result=0
    while(True):
        for  i in range(n):
            sq=sq+(array[i][temp[i]]*array[i][temp[i]])
        temp_result=sq%m
        if temp_result==m-1:
            result=temp_result
            break
        if result<temp_result:
            result=temp_result
        sq=0
        nxt=n-1
        while(nxt>=0 and (temp[nxt]+1>=len(array[nxt]))):
              nxt=nxt-1
        if(nxt<0):
              break
        temp[nxt]=temp[nxt]+1
        for i in range(nxt+1,n):
              temp[i]=0
        
    print(result)
n,m=map(int,input().split())
array=[]
for i in range(n):
    x=list(map(int,input().split()))
    array.append(x)
show(array,m)












