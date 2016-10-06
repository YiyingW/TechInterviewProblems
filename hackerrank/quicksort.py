'''
https://www.hackerrank.com/challenges/quicksort1

divide-and-conquer algorithm

divide:
	choose some pivot element, p, and partition your unsorted array into left, right, and equal,
		left < p, right > p, equal = p


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
	return (left + equal + right)

	

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)