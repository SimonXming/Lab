def RandomList(max):
	import random
	mylist=[]
	for i in range(0,max):
		mylist.append(random.randint(1,max))	
	print(mylist)
	return mylist

A=RandomList(10000)

def CountSort(A):
	C=[]
	B=[]
	for i in range(len(A)+1):
		C.append(0)
	for i in range(len(A)):
		B.append(0)

	for j in range(len(A)):
		C[A[j]]=C[A[j]]+1

	for i in range(1,len(C)):
		C[i]=C[i]+C[i-1]
	print(C)

	for j in range(len(A)-1,-1,-1):
		B[C[A[j]]-1]=A[j]
		C[A[j]]=C[A[j]]-1
	print(B)

R=CountSort(A)