import random
class Accumulator(object):
	"""docstring for Accumulator"""

	def __init__(self,num):
		super(Accumulator, self).__init__()
		self.total = 0.0
		self.N = num
	def addDataValue(self,value):
		self.total += value

	def mean(self):
		return(self.total/self.N)

		
x = Accumulator(100000)
for i in range(0,x.N):
	x.addDataValue(random.random())
print(x.mean())