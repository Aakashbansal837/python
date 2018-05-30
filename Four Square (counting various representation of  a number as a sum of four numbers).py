import math
def div(n):
	sum=0
	for i in range(1,int(math.sqrt(n))+1):
		if(n%i == 0):
			if(i*i == n and i%4!=0):
				sum = sum+i
				break
			if(i%4 !=0):
				sum = sum+i
			if((n/i)%4!=0):
				sum = sum+(n/i)
	return sum
	
	
t=int(input())
while(t>0):
	t-=1
	x=int(input())
 
	print(int(8*div(x)))
