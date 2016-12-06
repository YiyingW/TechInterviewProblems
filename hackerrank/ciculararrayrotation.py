'''
https://www.hackerrank.com/challenges/circular-array-rotation
'''

n, k, q = map(int, raw_input().split())

num_rotation = k%n 

'''
[1,2,3] 1
[3,1,2] 3
[2,3,1] 2
'''

l = map(int, raw_input().split())

query = []
for i in range(0, q):
	query.append(int(raw_input()))


for index in query:

	print l[(index-k)%n]