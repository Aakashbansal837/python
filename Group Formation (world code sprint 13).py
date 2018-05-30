#!/bin/python3

def membersInTheLargestGroups(n, m, a, b, f, s, t):
    mxs = [0, f, s, t]
    
    g,names = [],[]
    f = dict()
    for i in range(n):
        y, x = input().split()
        g += [int(x)]
        names += [y]
        f[y] = i
    
    p = [[x, 1 if g[x] == 1 else 0, 1 if g[x] == 2 else 0, 1 if g[x] == 3 else 0] for x in range(n)]
    
    def dsu_get(v):
        if p[v][0] != v:
            p[v][0] = dsu_get(p[v][0])
        return p[v][0]
    
    for _ in range(m):
        x, y = input().split()
        x = dsu_get(f[x])
        y = dsu_get(f[y])
        
        if x == y: continue
        
        total = 0
        for i in range(1, 4):
            cnt = p[x][i] + p[y][i]
            total += cnt
            if cnt > mxs[i]: total = b + 1
        
        if total <= b:
            p[x][0] = y
            p[y][1] += p[x][1]
            p[y][2] += p[x][2]
            p[y][3] += p[x][3]
    
    mx = -1
    for v in range(n):
        if a <= sum(p[dsu_get(v)][1:]) <= b:
            mx = max(mx, sum(p[dsu_get(v)][1:]))
    
    if mx == -1:
        print("no groups")
        return
    
    ans = []
    for v in range(n):
        if sum(p[dsu_get(v)][1:]) == mx:
            ans += [names[v]]
    
    for s in sorted(ans): print(s)

if __name__ == '__main__':
    nmabfst = input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])

    membersInTheLargestGroups(n, m, a, b, f, s, t)
