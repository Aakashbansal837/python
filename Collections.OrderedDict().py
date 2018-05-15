from collections import OrderedDict
dic= = OrderedDict()

for i in range(int(input())):
    arr = input().split(" ")
    key,value=[],0
    for j in arr:
        if j.isalpha():
            if len(key) == 0:
                key = j
            else:
                key = key+" "+j
        else:
            value = int(j)
    if key in dic:
        dic[key]+=value
    else:
        dic[key]=value

for k in dic:
    print(k,dic[k])
