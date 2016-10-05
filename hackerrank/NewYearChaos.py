'''
https://www.hackerrank.com/challenges/new-year-chaos
'''
import sys

def NewYearChaos(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in xrange(0, lastIndex):
        for j in xrange(0, lastIndex):
            if queue[j] > queue[j+1]:
                queue[j], queue[j+1] = queue[j+1], queue[j] 
                swaps += 1
                swaped = True      
        if swaped:
            swaped = False
        else:
            break
    return swaps

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    print NewYearChaos(q)




