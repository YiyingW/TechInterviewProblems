def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i 

# pay attention to how else is used here
# only return the first occurance of target in the seq
print find([1,3,5,7,2,1,3,5], 3)
