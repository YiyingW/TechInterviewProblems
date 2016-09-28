'''
https://www.hackerrank.com/challenges/non-divisible-subset
'''

n, k = map(int, raw_input().split())

arr = map(int, raw_input().split())

# create a dict to store the amount of nums for each mod
num_dic = {}

for i in range(0, k):
	num_dic[i] = 0

for i in range(0, n):
	mod = arr[i]%k
	num_dic[mod] += 1

subset = 0
if k%2 == 1:
	last_index = (k+1)/2 - 1  # 1, 2, 3, 4 // 1-4 2-3
	for i in range(1, last_index+1):
		subset += max(num_dic[i], num_dic[k-i])
	if num_dic[0] != 0:
		subset += 1
	print subset

if k%2 == 0:
	# 1, 2, 3, 4, 5, 6
	for i in range(1, k/2):
		subset += max(num_dic[i], num_dic[k-i])
	if num_dic[0] != 0: subset += 1
	if num_dic[k/2] != 0: subset += 1
	print subset



	