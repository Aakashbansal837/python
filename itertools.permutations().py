from itertools import permutations
a = input().split()
a[1] = int(a[1])
perms = [''.join(p) for p in permutations(sorted(a[0]),a[1])]
print (*perms,sep=("\n"))
