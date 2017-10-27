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
    def __init__(self):
        self.head=None

    def add_node_to_list(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            #make it a circular list
            self.head.next=self.head
        else:
            #declare a current var to store the head node.
            current=self.head
            #declare a previous var to store previous node.
            previous=current
            #while current next is not equal to the head
            #and current data is greater than the value
            #keep moving forward in the list.
            while current.next != self.head and current.data < value:
                #store the current in previous node.
                previous=current
                #move current to the next node.
                current = current.next

            if current.data > value:
                #you need to add this node right before current
                if previous != current:
                    #make the previous next point to current
                    previous.next=new_node
                #make the new node point to current
                new_node.next=current
                #if head was current, then make head point to the new node
                if self.head == current:
                    #walk to the end of the list and make sure to point it to the new node.
                    while(current.next != self.head):
                        current=current.next
                    #mark self head as new node
                    self.head = new_node
                    #mark the end of the tail to point to the new head
                    current.next=self.head

            elif current.data <= value:
                #add the new node after current
                #make sure you copy the current next to the new node next
                new_node.next = current.next
                #make current point to the new node
                current.next=new_node

    def print_all_the_nodes(self):
        current=self.head

        if current.next==self.head:
            print ("current.data=%d", current.data)
        else:
            while current.next != self.head:
                print ("current.data=%d",current.data)
                current=current.next
            print ("last data=%d", current.data)


    def test_cycle(self):
        node=self.head
        if node.next==self.head:
            return_value=self.has_cycle(node)
            print("has_cycle with node as %d returned %d" % (node.data, return_value))
        else:
            while node.next != self.head:
                return_value=self.has_cycle(node)
                print("has_cycle with node as %d returned %d" %(node.data,return_value))
                node = node.next

    def has_cycle(self,node):
        start=node
        is_cycle=-1

        if start == None:
            return is_cycle
        while start.next != node and start.next != None:
            start=start.next
        if start.next == node:
            is_cycle = 1
        return is_cycle


circular_list=single_circular_linked_list()
circular_list.add_node_to_list(10)
circular_list.add_node_to_list(4)
circular_list.add_node_to_list(6)
circular_list.add_node_to_list(2)
circular_list.add_node_to_list(20)
circular_list.print_all_the_nodes()
circular_list.test_cycle()

