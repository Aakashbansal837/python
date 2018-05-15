from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))
abc = list(product(A,B))
print (*abc)
