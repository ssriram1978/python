"""
Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def print_list(self):
        pointer = self.head
        output = ""
        while pointer:
            output += "{} ==>".format(pointer.value)
            pointer = pointer.next
        output += " None"
        print(output)

    def linkedlist_swap(self):
        first = self.head
        second = self.head.next
        while first and second:
            first.value, second.value = second.value, first.value
            if not second.next or not second.next.next:
                break
            first = second.next
            second = second.next.next

singly_linked_list = LinkedList()

for index in range(10):
    singly_linked_list.add_node(index)

singly_linked_list.print_list()

singly_linked_list.linkedlist_swap()

singly_linked_list.print_list()


