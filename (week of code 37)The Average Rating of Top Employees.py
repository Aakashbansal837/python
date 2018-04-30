from math import *
n=int(input())
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
summ=0;count=0
for i in a:
    if i>=90:
        summ+=i
        count+=1
result=summ/count
strr=list(str(result))
l=len(strr)
for i in range(l):
    if strr[i].isdigit():
        strr[i]=int(strr[i])
if (l>5):
    if strr[5] >=5:
        strr[4]+=1
if l >5:
    for i in range(5):
        print(strr[i],end='')
else:
    print("{:.2f}".format(result))

