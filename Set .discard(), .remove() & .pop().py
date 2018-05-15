n = int(input())
s = set(map(int, input().split()))
a = []
for i in range(int(input())):
    a = input().split()
    for _ in range(1,len(a)):
        a[_] = int(a[_])
    if a[0] == "remove":
        s.remove(a[1])
    if a[0] == "pop":
        s.pop()
    if a[0] == "discard":
        s.discard(a[1])
print(sum(s))
