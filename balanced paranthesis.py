def balanced(a):
    arr=[]
    for i in a:
        if (i == "{"):
            arr.append("}")
        elif (i == "["):
            arr.append("]")
        elif (i == "("):
            arr.append(")")
        else:
            l = len(arr)
            if l == 0 or i !=arr[l-1]:
                return False
            arr.pop()
    if len(arr) == 0:
        return True
    else:
        return False


def solve():
    n =int(input())
    for i in range(n):
        a = list(input())
        if balanced(a):
            print("YES")
        else:
            print ("NO")

solve()
