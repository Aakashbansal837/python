n = input()
a = input().split()
m = input()
b = input().split()
s1,s2 = set(a),set(b)
s3 = s1 ^ s2
print (len(s3))
