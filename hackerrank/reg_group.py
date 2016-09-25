'''
https://www.hackerrank.com/challenges/re-group-groups
'''

'''
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
'''

import re 


s = raw_input()

m = re.search(r'([a-zA-Z0-9])\1+', s)

if m != None:
	print m.group(0)[0]
else:
	print -1