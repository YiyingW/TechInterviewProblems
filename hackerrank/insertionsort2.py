'''
https://www.hackerrank.com/challenges/insertionsort2

utilize the insertionsort 1 to create the complete insertion sort function
'''

def subInsertionSort(arr, size, shift):
	e = arr[size-1]
	for i in range(size-1, -1, -1):
		this = arr[i-1]   
		if this > e and i != 0: # the smaller one is at back, shift
			arr[i] = this
			shift += 1
		elif this > e and i == 0: 
			arr[i] = this
			arr[0] = e
			return (arr, shift)
		else:
			arr[i] = e  # no shift
			return (arr, shift)
			break

s = int(raw_input())
ar = map(int, raw_input().strip().split())

shift = 0
for i in range(2, s+1):
	(ar[:i], shift) = subInsertionSort(ar[:i], i, shift)


	#print ' '.join(map(str, ar))
print shift 

	










