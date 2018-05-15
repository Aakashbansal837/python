import numpy as np
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)], dtype=int)
B = np.array([list(map(int, input().split())) for _ in range(N)], dtype=int)
print(np.add(A,B), np.subtract(A,B), np.multiply(A,B,), np.floor_divide(A,B), np.mod(A,B), np.power(A,B), sep = "\n")
