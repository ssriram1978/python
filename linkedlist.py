print("Demonstrate single linked list")
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

    def printList(self):
        temp=self.__head
        print("count=%d"%(self.__size))
        while temp != None:
            print("temp.object=",temp.object+"\n")
            temp=temp.next

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
list.push("Sriram")
list.push("Sridhar")
list.push("Srinivas")
list.push("Nithya")
list.push("Sriya")
print("list.printList=%s"%(list.printList()))
