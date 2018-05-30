total_fans, allowed_fans = (int(inp) for inp in input().split(' ')) #Taking th input as mentioned in the problem
hash_of_quotient_to_name = dict()
quotient_list=[]

#Storing the details in a dictionary by mapping the fan quotient to a list of names of fans with same fan quotient
i=1
while i<=total_fans:
	name_and_quotient_pair = input().split() 
	if quotient_list.__contains__(int(name_and_quotient_pair[1])): #If list contains the fan quotient then append the name
		hash_of_quotient_to_name[int(name_and_quotient_pair[1])].append(name_and_quotient_pair[0])
	else:
		hash_of_quotient_to_name[int(name_and_quotient_pair[1])]=[name_and_quotient_pair[0],]
		quotient_list.append(int(name_and_quotient_pair[1]))
	i+=1;

fans_list=[] #To store list of fans

for quotient in sorted(quotient_list)[::-1]: #Collecting the names of all the fans in sorted order
	for fan_name in sorted(hash_of_quotient_to_name[quotient]):
		fans_list.append(fan_name)


for i in range(allowed_fans):#Printing the names of fans
	print(fans_list[i])
