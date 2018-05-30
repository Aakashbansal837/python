def solve():
    stack = []
    maxx = 0
    top = 0
    for i in range(int(input())):
        a=[int(x) for x in input().split()]
        if a[0] == 1:
            top+=1
            stack.append(a[1])
            if maxx < a[1]:
                maxx = a[1]
        elif a[0] == 2:
            top-=1
            num = stack.pop()
            if num == maxx:
                if top == 0:
                    maxx = 0
                else:
                    maxx = max(stack)
        elif a[0] == 3:
            print(maxx)

solve()
