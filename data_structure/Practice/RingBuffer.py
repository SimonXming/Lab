#
#file name = RingBuffer.py
#date:2015.3.11
#author : Simon
#!/usr/bin/python
# -*- coding: utf-8 -*-

# l = [i for i in range(10)]
# while 1:
# 	for s in l:
# 		if s != l[len(l)-1]:
# 			print(s)
# 		else:
# 			print("????")
# 			break

class RingBuffer(object):
	"""docstring for ClassName"""
	def __init__(self,length):
		self.MAXSIZE = length
		self.readout = None
		self.writein = None
		self.data = [None for i in range(self.MAXSIZE)]

	def write(self,item):
		if self.data[self.MAXSIZE - 1] != None:
			print("Buffer is full,please try again later.")
			return 

		if self.writein != None:
			assert type(self.writein) == type(1)
			self.writein += 1
			self.readout = self.writein
			self.data[self.writein] = item
			return "write success"
		else:
			for i in range(self.MAXSIZE):
				if  self.data[i] != None:
					pass
				elif self.data[i] == None:
					self.data[i] = item
					self.writein = i
					self.readout = self.writein
					return "write success"

	def read (self):
		if self.data[0] == None:
			print("Buffer is Empty,please try again later.")
			return
		if self.readout != None:
			assert type(self.writein) == type(1)
			self.data[self.readout] = None
			self.readout -= 1
			self.writein = self.readout
			print(self.readout,self.writein)
			return "Read success." 

	def getlength(self):
		return len(self.data)

	def show(self):
		for i in range(self.getlength()):
			print(i,self.data[i])


if __name__ == '__main__':
	import sys
	L = RingBuffer(4)
	while 1:
		cmd = input("input:")
		if  cmd == "q":
			sys.exit(1)
		elif cmd == "w":
			inp = input("input what ?")
			L.write(inp)
			L.show()
		elif cmd == "r":
			print("Reading...Press enter.")
			L.read()
			L.show()
		else:
			print('''command error,please input "w","r","q"''')
