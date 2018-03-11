def result(lt,A):
    rl = []
    flag =0
    for i in range(len(A)):
        if(lt == A[i]):
            rl.append(i+1)
            flag+=1
    if (flag == 0):
        rl.append(-1)
    return rl
n,m = map(int,input().split())
A=[];B=[]
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
for i in range(m):
    l = result(B[i],A)
    print(*l)
