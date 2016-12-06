def question4(T, r, n1, n2):
	
	if n1 == n2:
		return n1
	if (r == None) or (n1==None) or (n2==None):
		return None
	min_val = min(n1, n2)
	max_val = max(n1, n2)

	current = r 

	while (current != None):
		if (current >= min_val) and (current <= max_val):
			return current 
		elif current > max_val:
			sublist = T[current][:current+1]
			current = [i for i,x in enumerate(sublist) if x == 1][0]			
		elif current < min_val:
			sublist = T[current][current:]
			current = [i for i,x in enumerate(sublist) if x == 1][0]


# case 1:
'''
		 3
		/ \
	   0   4          2 is isolated here
	    \  
	     1
'''
T1 = [[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]]

print question4(T1, 3, 1, 4)
# 3

# case 2:
'''
	0
	 \
	  1
'''
T2 = [[0, 1],
	  [0, 0]]
print question4(T2, 0, 0, 1)
# 0

# # case 3:
'''
      0
       \
        1
         \
          2
'''
T3 = [[0, 1, 0],
	 [0, 0, 1],
	 [0, 0, 0]]

print question4(T3, 0, 1, 2)
# # 1

# # case 4:
'''
	0
'''
T4 = [[0]]
print question4(T4, 0, 0, 0)
# # 0

# # case 5:
'''
		 3
		/ \
	   0   4          2 is isolated here
	    \  
	     1
'''
T5 = [[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]]

print question4(T5, 3, 1, 1)
# 1


