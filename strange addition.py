def rev(m):
    return (int("".join(list(reversed(list(str(m)))))))
     
def find():
    m,n =map(int,input().split())
    m = rev(m)
    n = rev(n)
    num = rev(m+n)
    print(num)
    

for i in range(int(input())):
    find()
