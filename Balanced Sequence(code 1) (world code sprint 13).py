#!/usr/bin/env python3

def main():
    N = int(input())
    S = input()
    R = []
    for s in S:
        if s==')' and len(R)>0 and R[-1]=='(':
            R.pop()
        else:
            R.append(s)
    # )^a + (^b
    a = R.count(')')
    b = len(R)-a
    if a==b==0:
        res = 0
    elif a==0 or b==0:
        res = 1
    else:
        res = 2
    print(res)

main()
