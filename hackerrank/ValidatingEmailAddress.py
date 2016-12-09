'''
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
print a list containing only valid email addresses in lexicographical order

valid email addresses:

1. It must have the username@websitename.extension format type
2. the username can only contain letters, digits, dashes and underscores
3. the website name can only have letters and digits
4. the maximum length of the extension is 3


a filter takes a function returning True or False and applies it to a sequence,
returning a list of only those members of the sequence where the function returned True.
A lambda function can be used with filters. 
'''
import re

# N = int(raw_input())
# emails = []
# for i in range(N):
#     emails.append(raw_input())

def validEmail(email):
    match = re.search(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{0,3}$', email)
    if match:
        return True
    else:
        return False
#validated = list(filter(lambda x: validEmail(x), emails))

#print sorted(validated)
print validEmail('harsh_@12gmail.co')


