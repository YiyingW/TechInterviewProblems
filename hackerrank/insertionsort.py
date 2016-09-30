'''
https://www.hackerrank.com/challenges/insertionsort1
'''

size = int(raw_input())
arr = map(int, raw_input().strip().split())

e = arr[size-1]
for i in range(size-1, -1, -1):
	this = arr[i-1]
	if this > e and i != 0:
		arr[i] = this
		print ' '.join(map(str, arr))
	elif this > e and i == 0:
		arr[i] = this
		arr[0] = e
		print ' '.join(map(str, arr))
	else:
		arr[i] = e
		print ' '.join(map(str, arr))
		break



