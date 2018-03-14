def solve():
    n =int(input())
    for i in range(n):
        arr =[];flag = 0
        a = list(input())
        for i in a:
            if (i == '{') or (i == '[') or (i == '('):
                arr.append(i)
                #print(arr)
            elif (i == '}') or (i == ']') or (i == ')'):
                if len(arr) != 0:
                    n = arr.pop()
                #print(arr)
                if n == "(" and i == ")":
                    flag = 1
                elif n == "[" and i == "]":
                    flag =1
                elif n == "{" and i == "}":
                    flag =1
                else:
                    flag=0
                    break
        if flag == 0 or len(arr) != 0:
            print("NO")
        else:
            print ("YES")

solve()
