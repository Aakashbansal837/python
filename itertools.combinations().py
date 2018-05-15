from itertools import combinations
s = input().split()
k = int(s[1])
for x in range (1,k+1):
    cmb =  (''.join(c) for c in combinations(sorted(s[0]),x))
    print (*cmb,sep = "\n")
