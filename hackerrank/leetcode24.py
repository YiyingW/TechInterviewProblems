'''
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the 
list, only nodes itself can be changed.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapTwoNodes(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val
        return None

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counter = 1
        currentNode = head
        while currentNode.next:
            nextNode = currentNode.next
            if counter % 2 == 1:
                self.swapTwoNodes(currentNode, nextNode)
                counter += 1
            else:
                counter += 1
            currentNode = nextNode

        return head


        