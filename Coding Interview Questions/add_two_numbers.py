#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

"""
Keep a pointer to each of the two singly linked list.
As they are already in reverse order,
sum the lsb. If there is a carry, just copy the lsb to a variable and keep the carry.
Move the pointers to the next location and do the same as told in the previous step but remember to add the carry.
Also, when you try to sum the current value to the previously computed value make sure to multiply the previous value by 10.
Now having computed the final sum. Prepare a linked list with the final output converted to string and return.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def print_list(self,node):
        while(node != None):
            print("%d->"%(node.val))
            node=node.next
        print("End\n")

    def translate_linked_list_to_num(self,linked_list):
        number=0
        if  linked_list == None:
            return -1
        MULT=10
        RAISE=0

        while(linked_list != None):
            number+= (linked_list.val * (MULT**RAISE))
            RAISE+=1
            linked_list=linked_list.next
        return number

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #declare two placeholders for two numbers.
        number1=0
        number2=0

        #do not process if the input params are invalid
        if l1 == None or l2 == None:
            return
        number1=self.translate_linked_list_to_num(l1)
        number2 = self.translate_linked_list_to_num(l2)
        sum=number1+number2
        list3=self.make_single_linked_list(sum)

        return list3

    def make_single_linked_list(self,number):
        head = None
        tail = None
        num_str=str(number)
        for index in range(len(num_str)-1,-1,-1):
            node = ListNode(int(num_str[index]))
            if head == None:
                head=node
                tail=head
            else:
                tail.next=node
                tail=node
        return head

sol=Solution()
list1=sol.make_single_linked_list(1111)
list2=sol.make_single_linked_list(222)
list3=sol.addTwoNumbers(list1,list2)
sol.print_list(list3)