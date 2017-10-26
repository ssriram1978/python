print("Demonstrate doubly linked list")
class linkedlist :
    __head=None
    __tail=None
    __size=0

    class Node:
        def __init__(self,object,next=None,prev=None):
            self.object=object
            self.next=next
            self.prev=prev

    def __init(self):
        self.__head=None
        self.size=0

    def length(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self,object):
        temp = self.Node(object,self.__head)
        #set the current head previous as this node.
        if self.__head != None:
            self.__head.prev = temp
        #set the head as the new node.
        self.__head=temp
        #set the tail to point to head.
        if self.__tail == None:
            self.__tail = self.__head
        #increment the current size by 1
        self.__size+=1

    def add_to_sorted_list(self,object):
        #add to the front if the list is empty
        if (self.__head == None):
            self.__head = self.__tail = self.Node(object)
            print("\nAdding %s to the beginning of the list" % (object))
        else:
            #locate the node which is greater than the passed in object
            temp=self.__head
            while(temp != None and temp.object < object):
                temp=temp.next
            #if you did not find any match then add it to the tail because the passed in object is the greatest.
            if(temp == None):
                temp = self.Node(object,None,self.__tail)
                self.__tail.next=temp
                self.__tail=temp
                print("\nAdding %s to the end of the list"%(object))
            #You found the node in the list which is greater than the passed in object.
            else:
                temp2 = self.Node(object,temp,temp.prev)
                temp3=temp.prev
                if(temp3 != None):
                    temp3.next=temp2
                temp.prev=temp2
                if (temp == self.__head):
                    self.__head = temp2
                print("\nAdding %s" %(object))
                print("before %s" %(temp.object))
                if (temp3 != None):
                    print("and after %s" %(temp3.object))
        self.__size += 1

    def delete_from_sorted_list(self,object):
        if(self.__head == None):
            return
        temp=self.__head
        while(temp != None):
            if(temp.object==object):
                #set the temp previous next to temp next
                if(temp.prev != None):
                    temp.prev.next=temp.next
                #set the temp next previous to point to temp prev
                if (temp.next != None):
                    temp.next.prev=temp.prev
                #set the head pointer and tail pointer accordingly
                if(self.__head == temp):
                    self.__head=temp.next
                if(self.__tail==temp):
                    self.__tail=temp.prev
                self.__size-=1
                print("\n Successfully deleted %s" %(object))
                return;
            temp = temp.next

    def reverse_linked_list(self):
        if(self.__head == None or  self.__tail == None):
            return
        previous_node=None
        next_node=None
        current_node=None
        prev_node=None

        current_node=self.__head

        # swap head and tail nodes.
        temp = self.__head
        self.__head = self.__tail
        self.__tail = temp

        while(current_node):
            #copy current's next node to next_node
            next_node=current_node.next
            #copy current's previous node to previous_node
            previous_node=current_node.prev
            #overwrite current's previous node with next_node
            current_node.prev=next_node
            #overwrite current's next node with previous_node
            current_node.next=prev_node
            #make sure to copy prev_node as the current node.
            prev_node=current_node
            #go to the next node and make the corresponding change.
            current_node=next_node


    def printList(self):
        temp=self.__head
        print("count=%d"%(self.__size))
        while temp != None:
            print("printList object=",temp.object+"\n")
            temp=temp.next

    def printListFromTail(self):
        temp=self.__tail
        print("count=%d"%(self.__size))
        while temp != None:
            print("printListFromTail: object=",temp.object+"\n")
            temp=temp.prev

    def enqueue(self,object):
        #make sure to make the new node previous point to tail.
        temp = self.Node(object,None,self.__tail)
        #set the tail next to point to this new node.
        self.__tail.next = temp
        self.__tail=temp
        self.__size+=1

    def dequeue_pop(self):
        temp=self.__head

        if temp!=None:
            if self.__head==self.__tail:
                self.__head=self.__tail=None
            else:
                #move the head
                self.__head=temp.next
                # make sure to current head points to the previous node as the new node.
                self.__head.prev = None
            self.__size=self.__size-1

        return temp.object

    def popTail(self):
        temp=self.__tail
        if self.__tail != None:
            if self.__head == self.__tail:
                self.__head=self.__tail=None
            else:
                #move the tail to point to the previous node.
                self.__tail=temp.prev
                #set the tail next to point to None
                self.__tail.next = None
            self.__size=self.__size-1
        return temp.object


list=linkedlist()
list.push("Sriram")
list.push("Sridhar")
list.push("Srinivas")
list.push("Nithya")
list.push("Sriya")
print("list.printList=%s"%(list.printList()))
list.enqueue("Home")
print("list.printList=%s"%(list.printList()))
print("list.dequeue_pop() ")
print(list.dequeue_pop())
print("list.printList=%s"%(list.printList()))
print("list.dequeue_pop() ")
print(list.dequeue_pop())
print("list.printList=%s"%(list.printList()))
print(list.dequeue_pop())
print("list.printList=%s"%(list.printList()))
print(list.dequeue_pop())
print("list.printList=%s"%(list.printList()))
print(list.popTail())
print("list.printList=%s"%(list.printList()))
print(list.popTail())
print("list.printList=%s"%(list.printList()))
print("add_to_sorted_list\n")
list.add_to_sorted_list("c")
list.add_to_sorted_list("d")
list.add_to_sorted_list("e")
list.add_to_sorted_list("a")
list.add_to_sorted_list("b")
print("list.printList=%s"%(list.printList()))
print("list.printListFromTail=%s"%(list.printListFromTail()))
print("delete_from_sorted_list\n")
list.delete_from_sorted_list("b")
print("list.printList=%s"%(list.printList()))
list.delete_from_sorted_list("d")
print("list.printList=%s"%(list.printList()))
list.delete_from_sorted_list("a")
print("list.printList=%s"%(list.printList()))
list.delete_from_sorted_list("e")
print("list.printList=%s"%(list.printList()))
list.delete_from_sorted_list("c")
print("list.printList=%s"%(list.printList()))

list.add_to_sorted_list("c")
list.add_to_sorted_list("d")
list.add_to_sorted_list("e")
list.add_to_sorted_list("a")
list.add_to_sorted_list("b")
print("list.printList=%s"%(list.printList()))
list.reverse_linked_list();
print("list.printList=%s"%(list.printList()))
print("list.printListFromTail=%s"%(list.printListFromTail()))