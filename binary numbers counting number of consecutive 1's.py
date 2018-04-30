n = int(input().strip())
n=list(bin(n))
count=1;count1=1
for i in range(1,len(n)):
    if n[i] == '1':
        if n[i-1] == '1':
            count1+=1
    elif n[i]=="0":
        if count < count1:
            count=count1
        count1 =1
if count < count1:
    count=count1        
print(count)
