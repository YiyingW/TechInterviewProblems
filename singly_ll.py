# a type declaration for a linked list of integers

# Node of a Singly Linked List

class Node:
    # constructor
    def__init__(self):
        self.data = None
        self.next = None

    # method for setting the data field of the node 
    def setData(self, data):
        self.data = data

    # method for getting the data field of the node
    def getData(self):
        return self.data

    # method for setting the next field of the node
    def setNext(self, nextNode):
        self.next = nextNode

    # method for getting the next field of the node
    def getNext(self):
        return self.next

    # returns true if the node points to another node
    def hasNext(self):
        return self.next != None


class SinglyLinkedList(): 
    def __init__(self):
	   self.head = None
	   self.length = 0

	# method for inserting a new node at the beginning of the linked list
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1






