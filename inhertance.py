class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores
    def calculate(self):
        total=0;
        for i in scores:
            total+=i
        r=total/(len(self.scores))
        if r>=90 and r<=100:
            return "O"
        elif r>=80 and r<90:
            return "E"
        elif r>=70 and r<80:
            return "A"
        elif r>=55 and r<70:
            return "P"
        elif r>=40 and r<55:
            return "D"
        elif r<40:
            return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
    
