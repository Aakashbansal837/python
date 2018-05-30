#!/bin/python3

import os
import sys

def addOne(x):
    return x+1

def minusOne(x):
    return x-1
# Complete the competitiveTeams function below.
def competitiveTeams(n, q):
    ingr = {}
    gr = {}
    for i in range(1,n+1):
        gr[i] = [i]
        ingr[i] = i
    c = {}
    c[1] = n
    C = [0, n]
    for i in range(n-1):
        C.append(0)
    teams = n
    for query in range(q):
        op = input().split()
        if int(op[0]) == 1:
            x = int(op[1])
            y = int(op[2])
            A = ingr[x]
            B = ingr[y]
            X = len(gr[A])
            Y = len(gr[B])
            if not A == B:
                if X > Y:
                    for elem in gr[B]:
                        gr[A].append(elem)
                        ingr[elem] = A
                    del gr[B]
                else:
                    for elem in gr[A]:
                        gr[B].append(elem)
                        ingr[elem] =  B
                    del gr[A]
                c[X] -= 1
                c[Y] -= 1
                if X in c.keys() and c[X] == 0:
                    del c[X]
                if Y in c.keys() and c[Y] == 0:
                    del c[Y]
                if X+Y in c.keys():
                    c[X+Y] += 1
                else:
                    c[X+Y] = 1
                newX = min(X,Y)
                newY = max(X,Y)
                C[:newX+1] = map(minusOne, C[:newX+1])
                C[newY+1:X+Y+1] = map(addOne, C[newY+1:X+Y+1])
                teams -= 1
                #print(c)
                #print(C)
        elif int(op[0]) == 2:
            #print(C)
            ct = int(op[1])
            if ct == 0:
                print(int(teams*(teams-1)/2))
            else:
                ans  = 0
                for i in c.keys():
                    if i+ct <= n:
                        ans = ans + C[i+ct] * c[i]
                print(ans)
    # Print the answer for each query of type 2. Take the query data from the standard input.

if __name__ == '__main__':
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    competitiveTeams(n, q)
