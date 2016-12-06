'''
stack
1 x -Push the element x into the stack
2   -Delete the element present at the top of the stack
3   -Print the maximum element in the stack
'''

s = []
maxval = 0
test = int(input())
for i in range(test):
    oper = raw_input()
    if oper[0] == "1":
        oper, element = oper.split()
        element = int(element)
        s.append(int(element))
        if maxval < element:
            maxval = element
    elif oper[0] == "2":
        temp = s.pop()
        if temp == maxval:
            maxval = 0
            if len(s) >= 1:
                maxval = max(s)
    else:
        print maxval