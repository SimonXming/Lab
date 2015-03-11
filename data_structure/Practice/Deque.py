#
#file name = Deque.py
#date:2015.3.8
#author : Simon
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/git-base/MyPyLib/MyPyLibary/data_structure/")
from double_linklist import LinkList

class Deque(object):
	"""Based on Double-LinkList,support method pushLeft,
	pushRight,popLeft,popRight,size.
	"""
	def __init__(self,data=[]):
		self.data = LinkList(data)

	def isEmpty(self):
		return self.data.is_empty()

	def size(self):
		return self.data.getlength()

	def pushLeft(self,item):
		self.data.deappend(item)

	def pushRight(self,item):
		self.data.append(item)

	def popLeft(self):
		self.data.delhead()

	def popRight(self):
		self.data.delend()

if __name__ == '__main__':
	x = Deque([1,2,3,4,5,6])
	print(x.isEmpty())
	print(x.size())
	x.pushLeft(10)
	print(x.size())
	x.pushRight("x")
	print(x.size())
	x.popLeft()
	print(x.size())
	x.popRight()
	print(x.size())
