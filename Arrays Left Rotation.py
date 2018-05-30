def array_left_rotation(a, k):
    a= a[k:] + a[:k]
    return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, k);
print(*answer, sep=' ')

