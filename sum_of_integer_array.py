numArray = map(int, input().split()) # Get the input


sum_integer = 0
# write your logic to add these 4 numbers here
sum_integer=numArray[4]
i = 4;
while i>0:
    sum_integer+=numArray[i-1]
    i-=1;



print(sum_integer) # Print the sum
