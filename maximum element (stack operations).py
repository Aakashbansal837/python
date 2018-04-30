def solve():
    stack = []
    for i in range(int(input())):
        a=input().split()
        a[0] = int(a[0])
        if a[0]==1:
            a[1] = int(a[1])
            stack.append(a[1])
        elif a[0] == 2:
            stack.pop()
        elif a[0]== 3:
            print(max(stack))
        

solve()
