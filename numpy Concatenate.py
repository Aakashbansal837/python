import numpy as np
n, m, p = map(int,input().split())
arrA = np.array([input().split() for _ in range(n)],int)
arrB = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((arrA, arrB), axis = 0))
