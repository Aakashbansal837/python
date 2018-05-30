for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in str(n)]
    count = 0
    for i in ar:
        if i != 0:
            if n%i == 0:
                count+=1
    print(count)
