queue=[]
t = int(input())
for i in range(t):
    num = [int(x) for x in input().split()]
    if num[0] == 3:
        print(queue[0])
    elif num[0] == 2:
        queue = queue[1:]
    elif num[0] == 1:
        queue.append(num[1])
        
