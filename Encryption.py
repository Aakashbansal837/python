from math import *
s = input();ll = len(s)
l = sqrt(ll)
f = floor(l)
c = ceil(l)
arr = [[]for i in range(c)]
i = 0;count = 0
while count < ll:
    arr[i].append(s[count])
    if i == c-1:
        i = 0
    else:
        i+=1
    count+=1
for i in arr:
    print("".join(i),end=" ")
