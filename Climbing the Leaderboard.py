n = int(input())
arr,brr =[int(x) for x in input().split()],[]
l=0;
for i in arr:
    if i not in brr:
        brr.append(i)
        l+=1
m = int(input())
crr = [int(x) for x in input().split()]
i=0
while(i<m):
    if crr[i] < brr[l-1]:
        print(l+1)
        i+=1
    elif l == 0:
        print(1)
        i+=1
    else:
        l-=1

