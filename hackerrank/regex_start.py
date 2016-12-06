'''
https://www.hackerrank.com/challenges/re-start-re-end
'''
import re


a_str = raw_input()
substr = raw_input()

p = re.compile(r"""
                    # zero-length match - empty string
(?=                 # positive lookahead assertion
(                   # group in lookahead to get start and end
"""+substr+"""      # concatenation to get pattern
)                   # closing parenthesis for lookahead group
)                   # closing parenthesis for lookahead assertion
""", re.VERBOSE)

if p.search(a_str):             # if there is any match
    for m in p.finditer(a_str): # for every Match object
        print((m.start(1), m.end(1)-1)) # start and end of group(1)
else:
    print((-1,-1))