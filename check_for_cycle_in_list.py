"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class single_circular_linked_list:
    def __init(self):
        self.head=None
    def add_node_to_list(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            #make it a circular list
            self.head.next=self.head
        else:
            current=self.head
            previous=current
            while current.next != self.head and current.data > value:
                previous=current
                current = current.next

            if current.next == self.head:
                #you reached the end
                if current.data < value:
                    #add it next to current
                    current.next=new_node
                    new_node.next=self.head
                else:
                    # add it before current
                    new_node.next=current
                    previous.next=new_node

            elif current.data <= value:
                # add it before current
                new_node.next = current
                previous.next = new_node


def has_cycle(head):
