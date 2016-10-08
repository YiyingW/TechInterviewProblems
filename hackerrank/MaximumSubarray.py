'''
https://www.hackerrank.com/challenges/maxsubarray


2 -1 2 3 4 -5

Kadane's algorithm:
a scan through the array values, computing at each position the maximum subarray
ending at that position. This subarray is either empty or consists of one more element
than the maximum subarray ending at the previous position. 
'''

def Contiguous(arr, n):
	if max(arr) < 0:
		return max(arr)
	result = [None]*n
	result[0] = arr[0]
	for i in range(1, n):
		if (result[i-1] + arr[i] < 0) or (result[i-1] < 0):
			result[i] = arr[i]
		else:
			result[i] = result[i-1]+arr[i]

	return max(result)

#  A better solution from wiki

def max_subarray(A):
	max_ending_here = max_so_far = A[0]
	for x in A[1:]:
		max_ending_here = max(x, max_ending_here+x)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def Non_contiguous(arr, n):
	if max(arr) < 0:
		return max(arr)
	result = 0
	for i in range(0, n):
		if arr[i] > 0:
			result += arr[i]
	return result 

T = int(raw_input())
for i in range(0, T):
	n = int(raw_input())
	arr = map(int, raw_input().split())
	print max_subarray(arr), 
	print Non_contiguous(arr, n)

# arr = [2,-1,2,3,4,-5]
# print Contiguous(arr, 6)


