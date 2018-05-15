import numpy
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
arr1 = numpy.array(a)
print (numpy.transpose(arr1))
print (arr1.flatten())
