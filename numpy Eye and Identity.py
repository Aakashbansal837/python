import numpy
a=[int(x) for x in input().split()]
print(str(numpy.eye(a[0],a[1],k=0)).replace("1."," 1.").replace("0."," 0."))
