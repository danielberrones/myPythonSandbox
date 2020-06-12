class Rectangle:
	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width

rectang = Rectangle(5,5)
print(rectang.area())