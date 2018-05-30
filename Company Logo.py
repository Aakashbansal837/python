dict={}

s = list(input())
for i in s:
    if i in dict:
        num = dict[i]
        num+=1
        dict[i] = num
    else:
        dict[i] = 1
dict = reversed(sorted(dict[i] for i in dict))
arr = list(dict[i] for i in dict)
print(arr)
count=0
for i in dict:
    if dict[i] == arr[0]:
        print(i,arr[0])
        count+=1
        if count == 3:
            break
    elif dict[i] == arr[1]:
        print(i,arr[1])
        count+=1
        if count == 3:
            break
    elif dict[i] == arr[2]:
        print(i,arr[2])
        count+=1
        if count == 3:
            break

