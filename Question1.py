'''
Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True. Your 
function definition should look like: question1(s, t) and return a boolean True or 
False.
'''

def question1(s, t):
	'''
	1. get the length of string t, l = len(t)
	2. create a hash table storing the letters in t and their occurance numbers
	3. slide a window with a length l in string s, put letters in that window into
		a dict, compare this dict with dict(t), if equal return True
	4. return False if no window has same dict with dict(t)

	'''
	l = len(t)
	dict_t = {}
	for letter in t:
		if letter not in dict_t.keys():
			dict_t[letter] = 1
		else:
			dict_t[letter] += 1

	for i in range(0, len(s)-l+1):
		sub_str = s[i:i+l]
		sub_dic = {}
		for letter in sub_str:
			if letter not in dict_t.keys():
				break # if found a letter that is not in t, break out of this window
			else:
				if letter not in sub_dic.keys():
					sub_dic[letter] = 1
				else:
					sub_dic[letter] += 1
		if sub_dic == dict_t: return True
	return False


print question1('', 'udacity')