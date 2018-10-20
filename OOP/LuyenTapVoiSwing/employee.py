
class Employee:

	raiseAmount = 1.07
	numOfEmp = 0

	def __init__(self, first = None, last = None, wage = 0):
		self.first = first
		self.last = last
		self.wage = wage
		self.email = first + last + '@gmail.com'
		Employee.numOfEmp += 1

	def outPut(self):
		print('My name is ' + self.first + ' ' + self.last + '\nMy wage is ' +
			 str(self.wage) + '\nemail : ' + self.email)

	@classmethod
	def setRaiseAmount(self, amount):
		self.raiseAmount = amount	

	@staticmethod
	def printHello():
		print('hello')	

employee1 = Employee('TranHuu', 'Thuy', 10000)
employee1.outPut()		

employee2 = Employee('PhanThanh', 'Phong', 20000)
employee2.outPut()	

print('Num Of Employees :',Employee.numOfEmp)

employee1.setRaiseAmount(1.05)

# employee1.raiseAmount = 1.05

print(Employee.raiseAmount)
print(employee1.raiseAmount)
print(employee2.raiseAmount)
