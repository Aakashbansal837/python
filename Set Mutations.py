n = int(input())
A = set(map(int,input().split()))
a = []
for _ in range(int(input())):
    a =input().split()
    if a[0] == "intersection_update":
        A.intersection_update(set(map(int,input().split() )))
    if a[0] == "symmetric_difference_update":
        A.symmetric_difference_update(set(map(int,input().split() )))
    if a[0] == "difference_update":
        A.difference_update(set(map(int,input().split() )))
    if a[0] == "update":
        A.update(set(map(int,input().split() )))
print (sum(A))
