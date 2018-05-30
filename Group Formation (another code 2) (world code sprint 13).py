#!/bin/python3


# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, minimum, b, f, s, t):
    grade = [0 for _ in range(n)]
    names = ["" for _ in range(n)]
    ids = {}
    sizes = [b, f, s, t]
    for i in range(n):
        name, g = input().split()
        grade[i] = int(g)
        names[i] = name
        ids[name] = i
    
    parent = [i for i in range(n)]
    size = [[1 if not i or g == i else 0 for g in grade] for i in range(4)]
    
    def get_parent(x):
        while parent[x] != x: x = parent[x]
        return x
    
    def join(a, b):
        a = get_parent(a)
        b = get_parent(b)
        if a == b: return
        for i in range(4):
            if size[i][a] + size[i][b] > sizes[i]: return
        
        if size[0][a] < size[0][b]: a, b = b, a
        parent[b] = a
        for i in range(4):
            size[i][a] += size[i][b]
    #print(size)
    for _ in range(m):
        left, right = input().split()
        a = ids[left]
        b = ids[right]
        join(a, b)
        #print(size)
    parent = [get_parent(i) for i in range(n)]
    
    val = max(size[0])
    if val < minimum:
        print("no groups")
        return
    res = []
    for i in range(n):
        if size[0][parent[i]] == val:
            res.append(names[i])
    for name in sorted(res):
        print(name)

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
