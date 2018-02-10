#Input: k = 3, n =  4
#list1 = 1->3->5->7->NULL
#list2 = 2->4->6->8->NULL
#list3 = 0->9->10->11
#Output:
#0->1->2->3->4->5->6->7->8->9->10->11
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.merged_list = []
        # compute the total number of linked lists
        self.total_number_of_linked_list = 0
        self.pointer_to_each_linked_list = []

    def computeMinNode(self):
        min_node=None
        min_index=-1
        if self.pointer_to_each_linked_list==None:
            return None

        #compute the min node by traversing the whole list
        for index in range(self.total_number_of_linked_list):
            if self.pointer_to_each_linked_list[index] == None:
                continue
            if min_node == None:
                min_node = self.pointer_to_each_linked_list[index]
                min_index=index
            else:
                if min_node.val > self.pointer_to_each_linked_list[index].val:
                    min_node = self.pointer_to_each_linked_list[index]
                    min_index=index

        if min_index >=0:
            #move the pointer to the next node because this node is going to get added to the final list
            self.pointer_to_each_linked_list[min_index]=self.pointer_to_each_linked_list[min_index].next
            # return the min node to the caller.
            return min_node
        else:
            return None

    def assign_pointers_to_each_linked_list(self,lists):
        #assign the pointers to the start of each linked list
        for index in range(self.total_number_of_linked_list):
            self.pointer_to_each_linked_list[index]=lists[index]

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None:
            return
        # compute the total number of linked lists
        self.total_number_of_linked_list = len(lists)
        self.pointer_to_each_linked_list = [0] * self.total_number_of_linked_list

        #assign a pointer to each of those singly linked lists.
        self.assign_pointers_to_each_linked_list(lists)

        isMerged=False
        prevNode=None
        while isMerged == False:
            #iterate all the linked lists to find the min element
            min_node=self.computeMinNode()
            if min_node != None:
                #create a new node and copy the content from the min node to this new node
                #print(min_node.val)
                new_node=ListNode(min_node.val)
                if prevNode == None:
                    self.merged_list.append(new_node)
                else:
                    prevNode.next=new_node
                prevNode = new_node
            else:
                isMerged=True

        return self.merged_list

lists=[]
def prepare_linked_list(start,end,increment):
    prevnode = None
    for index in range(start,end,increment):
        currentNode = ListNode(index)
        if prevnode == None:
            lists.append(currentNode)
        else:
            prevnode.next = currentNode
        prevnode = currentNode

def print_lists(linked_lists):
    for index in range(len(linked_lists)):
        linked_list=linked_lists[index]
        while linked_list:
            print("%d ->"%(linked_list.val),end=" ")
            linked_list=linked_list.next
        print("null\n")

prepare_linked_list(0,10,2)
prepare_linked_list(1,10,3)
prepare_linked_list(30,35,1)
prepare_linked_list(0,35,1)
#print(lists)
print_lists(lists)
sol=Solution()
merged_list = sol.mergeKLists(lists)
print_lists(merged_list)
