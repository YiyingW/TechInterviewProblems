'''
https://www.hackerrank.com/challenges/py-collections-namedtuple
'''

from collections import namedtuple 


num_students = int(raw_input())


Student = namedtuple('Student', raw_input())
values = []
for i in range(0, num_students):
	values.append(raw_input().split())


students = []

for i in range(0,num_students):
	this = Student(*values[i])
	students.append(this)

grade = 0
for stu in students:
	grade += float(stu.MARKS)
print "{:.2f}".format(grade/num_students) 
