
class Vector:

	def __init__(self, data):
		self.data = data

	def __str__(self):
		return super().__str__() + ' Vector'

	def __len__(self):
		return 1

	def __del__(self):
		pass

	def __add__(self, other):
		pass

	def __sub__(self, other):
		pass

vector = Vector([1, 2, 3])
print(vector.data)	

print(vector)	
print(len(vector))					