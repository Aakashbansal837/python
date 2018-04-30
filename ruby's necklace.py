b=int(input())
r=int(input())
y=int(input())
g=int(input())
count=0
pr=""
tmp1=b+r+g+y
tmp2=0
if b > 0:
    count+=1;pr="b";b-=1;tmp2+=1
elif r > 0:
    count+=1;pr="r";r-=1;tmp2+=1
elif y >0:
    count+=1;pr="y";r-=1;tmp2+=1
elif g >0:
    count+=1;pr="g";r-=1;tmp2+=1    
while(True):
    if r==0 and b==0 and g==0 and y ==0:
        break
    if pr == "g" or pr == "y":
        if r > 0:
            count+=1;pr="r";r-=1;tmp2+=1
        if g > 0:
            count+=1;pr="g";g-=1;tmp2+=1
    if pr =="r" or pr=="b":
        if y > 0:
            count+=1;y-=1;pr="y";tmp2+=1
        if b > 0:
            count+=1;b-=1;pr="b";tmp2+=1
    if tmp2>=tmp1:
        break
    
print(count)
