#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#For example,
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#Your algorithm should run in O(n) complexity.

from collections import defaultdict

class Solution:
    def __init__(self):
        self.hashtable=defaultdict(int)
        self.list_of_consecutive_integers=[]

    def createHashTable(self,nums):
        for number in nums:
            self.hashtable[number]=1

    def adjacent_elements(self,number,list,lesser):
        elem_found = True
        while elem_found == True:
            if number < 0:
                elem_found=False
            if lesser==True:
                number-=1
            else:
                number+=1
            #print("searching %d resulted "%(number) + str(self.hashtable[number]))
            if self.hashtable[number] == 0:
                elem_found = False
            else:
                list.append(number)
                #mark it to be true so that you skip the outer loop next time.
                #print("Marking %d in hashtable to be 2"%(number))
                self.hashtable[number]=2

    def find_adjacent_elements(self,number):
        list=[]
        #append the number to the list
        list.append(number)
        # keep searching the hash table until to find all the adjacent elements and keep adding them to a list.
        self.adjacent_elements(number,list,True)
        self.adjacent_elements(number,list,False)
        return list

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #create a hash table with the numbers
        self.createHashTable(nums)
    #iterate the hash table and get each element
        for number in nums:
            #for every element, search for its adjacent elements.
            if self.hashtable[number] == 2:
                #already processed this element.
                #print("skipping this %d because this is already processed."%(number))
                continue
            #mark this element as processed in the hash table.
            self.hashtable[number]=2
            #declare a list to capture all the consecutive elements
            list=self.find_adjacent_elements(number)
            #append this list to the list_of_consecutive_integers
            if len(list) > 0:
                self.list_of_consecutive_integers.append(list)

        print(self.list_of_consecutive_integers)
        largest_list=0
        for items in self.list_of_consecutive_integers:
            if largest_list < len(items):
                largest_list=len(items)

        return largest_list
    #return the largest consecutive element sequence

sol=Solution()
input_list=[100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(input_list))