'''
https://www.hackerrank.com/challenges/insertionsort2

utilize the insertionsort 1 to create the complete insertion sort function
'''

def subInsertionSort(arr, size):
	e = arr[size-1]
	for i in range(size-1, -1, -1):
		this = arr[i-1]
		if this > e and i != 0:
			arr[i] = this
		elif this > e and i == 0:
			arr[i] = this
			arr[0] = e
			return arr
		else:
			arr[i] = e
			return arr
			break

s = int(raw_input())
ar = map(int, raw_input().strip().split())

for i in range(2, s+1):
	ar[:i] = subInsertionSort(ar[:i], i)
	print ' '.join(map(str, ar))
	










