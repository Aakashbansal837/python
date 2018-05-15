dict={}
n = int(input())
for i in range(n):
    a,b = input().split()
    dict[a] = int(b)
while(True):
    name=input()
    if (name.strip() == ""):
        break
    else:
        if name in dict:
            print(name,"=",dict[name],sep="")
        else:
            print("Not found")
