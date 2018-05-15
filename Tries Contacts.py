arr=[]
n = int(input())
for i in range(n):
    tmp = input().split()
    if tmp[0] == "add":
        arr.append(tmp[1])
    elif tmp[0] == "find":
        num = tmp[1]
        l = len(num)
        count = 0
        for i in arr:
            j=0
            while(j < l):
                if num[j] != i[j]:
                    break
                else:
                    j+=1
            if j == l:           
                count+=1
        print(count)
