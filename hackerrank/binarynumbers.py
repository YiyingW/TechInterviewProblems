'''
convert a decimal number to binary number 

114 = 64 + 50 = 64 + 32 + 18 = 64 + 32 + 16 + 2 => 1110010

114:2=57 remainder 0
57:2=28 remainder 1
28:2=14 remainder 0
14:2=7 remainder 0
7:2=3 remainder 1
3:2=1 remainder 1
1:2=0 remainder 1
'''

def binaryConverter(n):
	binary=[]
	while (n!=0):
		binary.append(n%2)
		n = n/2
	binary.reverse()
	binary = map(str, binary)
	return "".join(binary)

print binaryConverter(114)

