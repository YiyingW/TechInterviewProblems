'''
https://www.hackerrank.com/challenges/fibonacci-modified

ti+2 = ti + (ti+1)^2
0, 1, 1, 2, 5, 27, ... 

given t1, t2, and n, compute and print term tn of a modified Fibonacci seq
'''

def FibModified(t1, t2, n):
	seq = [t1, t2]
	for i in range(2, n):
		seq.append(seq[i-2] + seq[i-1]**2)
	#print seq
	return seq[-1]

t1, t2, n = map(int, raw_input().split())
print FibModified(t1, t2, n)
