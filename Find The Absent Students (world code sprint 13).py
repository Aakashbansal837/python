#------------- my code-----------
n = int(input())
arr1=[int(x) for x in input().split()]
arr=[]
for i in range(1,n+1):
    if i not in arr1:
        arr.append(i)
print(len(arr))

#-----------setter code ----------------
def solve(n, a):
    solution = []
    for x from 1 to n:
        found = False
        for i from 1 to n:
            if x == a[i]:
                found = True
        if not found:
            solution.append(x)

    print (solution)
#-----------tester code ----------------
print(*sorted(set(range(1, 1 + int(input()))) - set(map(int, input().split()))))
