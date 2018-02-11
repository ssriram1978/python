"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
1. start from the end of the list and keep looking for first decreasing element.
2. Starting from that position, look forward to find the element just larger than the element found at step1.
or
starting from the end of the list, search backwards to find the element that is larger than the element found at step1.
3. swap elements found at step1 and step2.
4. If you did not find any element at step1, then, reverse the list by keep swapping the elements at
 the edge as you traverse inwards.
"""

class Solution:
    def swap(self,nums,index1,index2):
        temp=nums[index1]
        nums[index1]=nums[index2]
        nums[index2]=temp

    def reverse(self,nums,starting_index):
        ending_index=len(nums)-1
        while starting_index<ending_index:
            self.swap(nums,starting_index,ending_index)
            starting_index+=1
            ending_index-=1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums==None:
            return
        next_permutation=[]
        found_a_smallest_num=False
        for index in range(len(nums)-2,-1,-1):
            #search for a number that is less than the end element
            if nums[index] < nums[index+1]:
                found_a_smallest_num=True
                break

        found_a_larger_number=False
        if found_a_smallest_num==True:
            #go and find a element larger than the found element.
            for index2 in range(len(nums)-1,index-1,-1):
                if nums[index2] > nums[index]:
                    found_a_larger_number=True
                    break
            if found_a_larger_number == True:
                #swap the numbers
                self.swap(nums,index,index2)
        #reverse all the elements from the end to the location where you found the starting number
        self.reverse(nums,index+1)
        #print(nums)

sol=Solution()
array=[1,2,3]
for index in range(10):
    sol.nextPermutation(array)
    print(array)
