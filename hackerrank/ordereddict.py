# An orderedDict is a dictionary that remembers the order of the keys that
# were inserted first. If a new entry overwrites an existing entry, the 
# original insertion position is left unchanged. 

import sys
from collections import OrderedDict

'''
https://www.hackerrank.com/challenges/py-collections-ordereddict
Taks: you are the manager of a supermarket
you have a list of N items together with their prices that consumers bought
on a particular day. your task is to print each item_name and net_price
in order of its first occurence. 
'''

amount = int(input())

item_dict = OrderedDict()

for line in sys.stdin:
	inputs = line.split()
	if len(inputs) == 0:
		break
	price_loc = len(inputs)-1
	price = int(inputs[price_loc])
	name = " ".join(inputs[:price_loc])

	if name in item_dict:
		item_dict[name] = price + item_dict[name]
	else:
		item_dict[name] = price


for name, price in item_dict.items():
	print (name, price)