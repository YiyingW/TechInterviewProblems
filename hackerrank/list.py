'''
https://www.hackerrank.com/challenges/python-lists
'''

N = int(raw_input())

l = []

for i in range(0, N):
	command = raw_input().split()
	if command[0] == 'print':
		print l 
	elif command[0] == 'insert':
		index = int(command[1])
		num = int(command[2])
		l.insert(index, num)
	elif command[0] == 'remove':
		l.remove(int(command[1]))
	elif command[0] == 'append':
		l.append(int(command[1]))
	elif command[0] == 'sort':
		l.sort()
	elif command[0] == 'reverse':
		l.reverse()
	else:
		l.pop()

