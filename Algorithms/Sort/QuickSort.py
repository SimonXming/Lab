def RandomList(max):
	import random
	mylist=[]
	for i in range(0,max):
		mylist.append(random.randint(1,max))	
	print(mylist)
	return mylist

A=RandomList(100)

def Partition(seq,p,r):
	x=seq[r]
	i=-1
	for j in range(0,r):
		if seq[j]<=x:
			i+=1
			key=seq[i]
			seq[i]=seq[j]
			seq[j]=key
	key2=seq[i+1]
	seq[i+1]=seq[r]
	seq[r]=key2
	return(i+1)


def QuickSort(seq,p,r):
	if p<r:
		q=Partition(seq,p,r)
		QuickSort(seq,p,q-1)
		QuickSort(seq,q,r)
	return(seq)

result=QuickSort(A,0,len(A)-1)
print(result)