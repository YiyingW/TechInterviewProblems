'''
https://www.hackerrank.com/challenges/greedy-florist

'''

N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1

result = 0

if N <=K:
	print sum(C)
else:
	C = sorted(C, reverse=True)
	cycle = N/K
	module = N%K
	for x in range(0, cycle):
		for i in range(0, K):
			result += (x+1)*C[i+x*K]
	for i in range(0, module):
		result += (cycle+1)*C[i+cycle*K]
print result