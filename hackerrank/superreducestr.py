s = 'aaabccddd'
ls = list(s)

NotDone = True

while(NotDone):
	NotDone = False
	for i in range(0, len(ls)-1):
		if ls[i] == ls[i+1]:
			NotDone = True
			ls[i] = 0
			ls[i+1] = 0
			ls = [l for l in ls if l != 0]
			break


if len(ls) == 0:
	print 'Empty String'
else:
	print ''.join(ls)
