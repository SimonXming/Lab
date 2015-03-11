#file name = Josrphus.py
#date:2015.3.11
#author : Simon
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import deque

def josephus(self):
	queue = deque([])
	totle_number = int(sys.argv[1])
	bad_lucky = int(sys.argv[2])
	for i in range(totle_number):
		queue.append(i)

	while len(queue) != 0:
		for i in range(1,bad_lucky+1):
			if i != bad_lucky:
				queue.append(queue.popleft())
			else:
				print(queue.popleft())

if __name__ == '__main__':
	josephus()