#!/bin/python

import os
import sys

# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, a, b, f, s, t, people, requests):
    max_grade = [f, s, t]
    person_id = {x: i for i, x in enumerate(sorted(people.keys()))}
    id_person = sorted(people.keys())
    par = [i for i in range(n)]
    size = [1]*n
    count = [[0]*3 for _ in range(n)]
    for person, grade in people.items():
        count[person_id[person]][int(grade)-1] = 1
    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
    def union(x, y):
        if size[x] < size[y]:
            return union(y, x)
        size[x] += size[y]
        count[x] = [count[x][i] + count[y][i] for i in range(3)]
        par[y] = x
    for x, y in requests:
        x, y = person_id[x], person_id[y]
        x, y = find(x), find(y)
        if x == y: continue
        if size[x] + size[y] > b: continue
        if any(count[x][i] + count[y][i] > max_grade[i] for i in range(3)): continue
        union(x, y)
    groups = []
    for i in range(n):
        if par[i] != i: continue
        if size[i] < a: continue
        groups.append(i)
    if len(groups) == 0:
        print 'no groups'
    else:
        max_size = max(size[x] for x in groups)
        good_groups = set(x for x in groups if size[x] == max_size)
        result = [i for i in range(n) if find(i) in good_groups]
        print '\n'.join(sorted([id_person[x] for x in result]))
        

if __name__ == '__main__':
    nmabfst = raw_input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])
    
    people = dict([tuple(raw_input().split()) for _ in range(n)])
    requests = [raw_input().split() for _ in range(m)]

    membersInTheLargestGroups(n, m, a, b, f, s, t, people, requests)
