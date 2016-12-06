'''
each person has a first name, last name, age and sex
print their names in a specific format sorted by their age in ascending order
if two people have same age, print them in the order of their input. 

convert Male to Mr. someone
Female to Ms. someone

'''
from operator import itemgetter

N = int(raw_input())
people=list()
for i in range(N):
	people.append(str(raw_input()).split())

def sortbyage(f):
	def input(people):
		newinfo = [f(oldinfo) for oldinfo in people]
		newinfo.sort(key=itemgetter(1))
		#print newinfo
		return newinfo
	return input


@sortbyage
def newName(nameinfo): # input is a list of four items
	if nameinfo[3] == "M":
		return ["Mr. "+nameinfo[0]+" "+nameinfo[1], int(nameinfo[2])]
	else:
		return ["Ms. "+nameinfo[0]+" "+nameinfo[1], int(nameinfo[2])]

newnames = newName(people)
for name in newnames:
	print name[0] + " " + str(name[1])