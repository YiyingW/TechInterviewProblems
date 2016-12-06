'''
https://www.hackerrank.com/challenges/re-findall-re-finditer

[b-df-hj-np-tv-z] all the consonants
'''

import re 

s = raw_input()

result = re.findall(r'(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z +-]{1})([AEIOUaeiou]{2,})(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z +-]{1})',s)

if len(result) == 0:
	print -1
else:
	for i in result:
		print i 


'''
solution:


import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
if match:
    for i in match:
        print i
else:
    print -1

'''