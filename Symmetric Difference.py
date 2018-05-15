m = int(input())
list_a = map(int, input().split())
n = int(input())
list_b = map(int, input().split())
set1,set2 = set(list_a), set(list_b)
result = set1 ^ set2
new = sorted(result)
for _ in range(len(new)):
    print (new[_])
