import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split())

def bubblesort(n, a):
	totalswap = 0
	for i in range(0, n):
		numOfSwaps = 0
		for j in range(0, n-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				numOfSwaps += 1
				totalswap += 1
		if numOfSwaps == 0:
			break
	return (a, totalswap)

sorted_a, swap = bubblesort(n, a)
print "Array is sorted in {} swaps.".format(swap)
print "First Element: {}".format(sorted_a[0])
print "Last Element: {}".format(sorted_a[-1])