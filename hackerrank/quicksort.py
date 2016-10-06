'''
https://www.hackerrank.com/challenges/quicksort1

divide-and-conquer algorithm

divide:
	choose some pivot element, p, and partition your unsorted array into left, right, and equal,
		left < p, right > p, equal = p
If partition is then called on each sub-array, the array will now be split into four parts.
This process can be repeated until the sub-arrays are small. When partition is called on just
one of the numbers, they end up being sorted.

'''

def partition(ar):
	p = ar[0]
	left = []
	equal = [p]
	right = []
	for i in range(1, len(ar)):
		if ar[i] < p:
			left.append(ar[i])
		elif ar[i] == p:
			equal.append(ar[i])
		else:
			right.append(ar[i])

	return (left, equal, right)

	
def sort(arr):
	if len(arr) < 2: return arr 
	if len(arr) == 2:
		if arr[0] > arr[1]:
			arr[0], arr[1] = arr[1], arr[0]
			return arr
		else:
			return arr
	if len(arr) > 2:
		left, p, right = partition(arr)		
		final = sort(left) + p + sort(right)
		return final 


m = input()
ar = [int(i) for i in raw_input().strip().split()]

print sort(ar)
