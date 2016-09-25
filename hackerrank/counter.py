'''
https://www.hackerrank.com/challenges/collections-counter
'''

# populate the shoe list

from collections import Counter

shoes_amount = int(raw_input())

shoes = map(int,raw_input().split())


customer_amount = int(raw_input())

need = []
for i in range(0, customer_amount):
	this = raw_input().split()
	need.append([int(this[0]), int(this[1])])


shoes_counts = Counter(shoes)

income = 0
for c in need:
	shoe = c[0]
	price = c[1]
	if shoe in shoes_counts.keys():
		if shoes_counts[shoe] > 0:
			income += price
			shoes_counts[shoe] -= 1

print income
