#
#file name:linklist.py
#date:2014.10.14
#author : Simon
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):


	def __init__(self,val,p=0):
		self.data = val
		self.next = p


class LinkList(object):


	def __init__(self,data=[]):
		if data ==[]:
			self.head = 0
		else:
			self.head = Node(data[0])
			p = self.head
			for i in data[1:]:
				node = Node(i)
				p.next = node
				p = p.next

	def __getitem__(self,key):
		if self.is_empty():
			print('linklist is empty.')
			return
		elif key < 0  or key > self.getlength():
			print('the given key is error')
			return
		else:
			return self.getitem(key)

	def __setitem__(self,key,value):
		if self.is_empty():
			print('linklist is empty.')
			return
		elif key < 0  or key > self.getlength():
			print('the given key is error')
			return
		else:
			self.delete(key)
			return self.insert(key)

	def __iter__(self):
		print("__iter__ called") 
		self.append(0)
		return self

	def __next__(self):
		if self.is_empty() :
			print("Empty")
			raise StopIteration  
		else:
			self.delete(self.getlength() - 1)
			return self

	def __str__(self):
		return str(self.getitem(self.getlength() - 1))

	def initlist(self,data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next

	def getlength(self):
		length = 0
		p =  self.head
		while p != 0:
			length+=1
			p = p.next
		return length

	def is_empty(self):
		if self.getlength() == 0:
			return True
		else:
			return False

	def clear(self):
		self.head = 0

	def append(self,item):
		q = Node(item)
		if self.head == 0:
			self.head = q
		else:
			p = self.head
			while p.next != 0:
				p = p.next
			p.next = q

	def getitem(self,index):
		if self.is_empty():
			print ('Linklist is empty.')
			return
		j = 0
		p = self.head
		while p.next != 0 and j < index:
			p = p.next
			j+=1
		if j == index:
			return p.data
		else:
			print ('target is not exist!')

	def insert(self,index,item):
		if self.is_empty() or index < 0 or index > self.getlength():
			print ('Linklist is empty.')
			return
		if index == 0:
			q = Node(item,self.head)
			self.head = q
			return
		j = 0		
		p = self.head
		post  = self.head
		while p.next != 0 and j < index:
			post = p
			p = p.next
			j+=1
		if index == j:
			q = Node(item,p)
			post.next = q
			q.next = p

	def delete(self,index):
		if self.is_empty() or index < 0 or index > self.getlength():
			print ('Linklist is empty.')
			return
		if index == 0:
			q = self.head
			self.head = q.next
			return
		j = 0		
		p = self.head
		post  = self.head
		while p.next != 0 and j < index:
			post = p
			p = p.next
			j+=1
		if index ==j:
			post.next = p.next

	def index(self,value):
		if self.is_empty():
			print ('Linklist is empty.')
			return
		i = 0
		p = self.head
		while p.next != 0 and not p.data == value:
			p = p.next
			i+=1
		if p.data == value:
			return i
		else:
			return -1

if __name__ == '__main__':
	l=LinkList([7,3,10,4,5])
	# llist=[7,3,10,4,5,]
	# l.initlist(llist)
	print(l.getlength())
	l.insert(0,1)
	for i in l:
		print(i)
	# print(l.delete(0))

	# l.append(11)
	# l.insert(2,100)

	# print(l.getlength())
	# print(l.getitem(0))
	# for i in range(l.getlength()):
	# 	print(l.index(llist[i]))
	# l.clear()
	# print(l.getlength())



		

