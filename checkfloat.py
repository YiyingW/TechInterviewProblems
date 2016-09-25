'''
[+-]?  optional, either + or -
\d*  zero or more digits
\.  dot 
\d+  one or more digits
$ end of string
'''

import re
for i in range(int(raw_input())):
    print bool(re.search(r"^[+-]?\d*\.\d+$",raw_input().strip()))