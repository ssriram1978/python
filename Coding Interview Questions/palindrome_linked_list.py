"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def addNodeToSinglyLinkedList(self,value):
        node = ListNode(value)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=node

    def printSinglyLinkedList(self):
        temp=self.head
        while temp != None:
            print(str(temp.val) + "->",end=" ")
            temp=temp.next
        print("None",end=" ")

list=SinglyLinkedList()
list.addNodeToSinglyLinkedList(10)
list.addNodeToSinglyLinkedList(40)
list.addNodeToSinglyLinkedList(50)
list.printSinglyLinkedList()

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Given a singly linked list,
        1. Have a fast and slow pointer.
        2. For every traversal of the list, Fast pointer jumps 2 steps ahead of the slow pointer.
        3. When Fast pointer reaches the end of the list, slow pointer will be at the mid of the list.
        4. Now, take another pointer X pointing to the start of the original list.
            Until slow pointer is equal to the fast pointer.
                Compare if the content of X and the start pointer are the same
                If they are same, continue with the next item in the list until you reach end of the list and
                return True if they match.
                Else:
                Return False.
        """
