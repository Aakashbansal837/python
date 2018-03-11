def solve():
    k, mod = [int(x) for x in input().split()]
    n = []
    for i in range(k):
        n.append([(int(x)**2) % mod for x in input().split()[1:]])

    a = set(n[0])
    if k == 1:
        return max(a)

    for i in range(1, k - 1):
        temp1 = set()
        for j in range(len(n[i])):
            temp2 = set()
            for l in a:
                temp2.add((l + n[i][j]) % mod)

            temp1 = temp1.union(temp2)

        a = a.union(temp1)

    maxx = 0
    for i in range(len(n[k - 1])):
        for l in a:
            maxx = max(maxx, (n[k - 1][i] + l) % mod)

    return maxx

print(solve())
