#
#file name = Steque.py
#date:2015.3.1
#author : Simon
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/git-base/MyPyLib/MyPyLibary/data_structure/")
from linklist import LinkList

class Steque(object):
	"""Based on LinkList,support method push,pop,enqueue,size.
	"""
	def __init__(self,data=[]):
		self.data = LinkList(data)

	def push(self,item):
		self.data.append(item)

	def pop(self):
		memo = self.data.getlength() - 1
		self.data.delete(self.data.getlength() - 1)
		return memo

	def enqueue(self,item):
		self.data.insert(0,item)

	def size(self):
		return self.data.getlength()

if __name__ == '__main__':
	x = Steque([1,2,3,4,5])
	print(x.size())
	x.push(6)
	print(x.size())
	print(x.pop())
	x.enqueue(83)
	print(x.size())
