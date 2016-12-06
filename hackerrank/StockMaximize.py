'''
https://www.hackerrank.com/challenges/stockmax
'''

'''
find the maximum number in the array, buy everyday before that day, sell all on 
that day. Array is reduced. Do the same thing again until the maximum is at the
front or the array has length 0
'''
import numpy as np 



def solution(arr):

	def buyStock(arr):
		max_value = max(arr)
		idx = [i for i in range(0, len(arr)) if arr[i] == max_value][0]
		buy = 0
		count = 0
		for i in range(0, idx):
			buy = buy+arr[i]
			count += 1
		profit = count*arr[idx] - buy
		return (profit, idx)

	result = 0
	while (len(arr) > 0):
		profit, idx = buyStock(arr)
		idx += 1
		result += profit
		arr = arr[idx:]
	return result


arr = np.array([5,3,2])
print solution(arr)

