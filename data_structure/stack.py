#
#file name:stack.py
#Date:2015.3.3
#Author:Simon
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:
	"""Simple Stack data structure."""

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0
   
	def push(self, item):
		self.items.append(item)
   
	def pop(self):
		return self.items.pop()
   
	def peek(self):
		if not self.isEmpty():
			return self.items[len(self.items) - 1]
     
	def size(self):
		return len(self.items) 

class LinkStack:
	"""Simple Stack data structure."""

	def __init__(self):
		self.items = LinkList()

	def isEmpty(self):
		return self.items.is_empty()
   
	def push(self, item):
		self.items.append(item)
   
	def pop(self):
		memo = self.items.getlength() - 1
		self.items.delete(self.items.getlength() - 1)
		return memo
   
	def peek(self):
		if not self.isEmpty():
			return self.items[self.items.getlength() - 1]
     
	def size(self):
		return self.items.getlength()

if __name__ == '__main__':
	import sys
	sys.path.append("/home/git-base/MyPyLib/MyPyLibary/data_structure/")
	from linklist import LinkList
	l = LinkStack()
	for i in range(4):
		print(i)
		l.push(i)
	print("l.isEmpty()",l.isEmpty())
	print("l.size()",l.size())
	print("pop",l.pop())
	print("size",l.size())
	print("peek",l.peek())