s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
apple=[int(x) for x in input().split()]
orange=[int(x) for x in input().split()]
print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))
