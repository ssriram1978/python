"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

# declare three nodes. current, previous, next
# prev is used to keep track of the previous node in the while loop
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    head=None
    def __int__(self):
        self.head=None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # boundary check
        if self.head == None or self.head.next == None:
            return head

        # declare three nodes. current, previous, next
        # prev is used to keep track of the previous node in the while loop
        prev = None
        # declare current as head
        current = self.head
        # declare next which is used as a temporary node to move on to the next node.
        next = None

        while current != None:
            # copy current.next to next
            next = current.next
            # overwrite current.next to point to previous node
            current.next = prev
            # make previous node as current node
            prev = current
            # copy back next node to current node so that you move on to the next node.
            current = next

        #after exiting the while loop, make sure to move head to the prev node.
        self.head=prev

        return self.head

    def constructSingleLinkedList(self,node):
        # boundary check
        if node == None:
            return

        #assign it to head if it is none.
        if self.head == None:
            self.head=node
            return

        #move to the end of the list
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=node

    def printSingeLinkedList(self):
        # boundary check
        if self.head == None:
            return
        temp = self.head
        while temp != None:
            print("node=%d" %(temp.val))
            temp = temp.next


sol=Solution()
for number in range(1,10,+1):
    node=ListNode(number)
    sol.constructSingleLinkedList(node)
sol.printSingeLinkedList()
sol.reverseList(sol.head)
sol.printSingeLinkedList()
