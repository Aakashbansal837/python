def prime(n):
    i = 2
    num = n//2
    while(i < num):
        if n%i == 0:
            return False
        else:
            i+=1
    return True

n = int(input())
for i in range(n):
    num = int(input())
    if prime(num):
        print("Prime")
    else:
        print("Not prime")
