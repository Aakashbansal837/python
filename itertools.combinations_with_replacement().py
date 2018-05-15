from itertools import combinations_with_replacement
s = input().split()
s[1] = int(s[1])
lst = [''.join(x) for x in combinations_with_replacement(sorted(s[0]),s[1])]
print(*lst,sep="\n")
