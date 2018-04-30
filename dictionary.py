def solve():
    d  =[]
    for _ in range(int(input())):
        lst = input().split()
        d.append(lst)
    while(True):
        qrr = input()
        if qrr == ".":
            break
        else:
            for i in range(len(d)):
                if qrr == d[i][0]:
                    print(qrr,"=",d[i][1])
                    break

solve()
