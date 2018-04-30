class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code her
    def computeDifference(self):
        arr=self.__elements
        l=len(arr)
        r=0
        for i in range(l-1):
            for j in range(i+1,l):
                num=abs(arr[i]-arr[j])
                if r <num:
                    r=num
        global maximumDifference
        maximumDifference = r
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
