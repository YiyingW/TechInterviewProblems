'''
https://www.hackerrank.com/challenges/30-linked-list

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data
            current = current.next

    def insert(self, head, data):
        currentNode = head
        print 'here'
        toInsert = Node(data)
        if currentNode == None:
            return toInsert
        else:
            print 'current not none'
            nextNode = currentNode.next
            while nextNode:
                print 'in while loop'
                currentNode = currentNode.next
                nextNode = currentNode.next
            currentNode.next = toInsert
        return head 

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);