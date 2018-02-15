"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #declare the output return list
        return_list = []
        #declare three indexes for the 3 numbers to be found.
        index_1=0
        index_2=0
        index_3=0
        #start a while loop for the first index to be searched
        for index_1 in range(len(nums)) :
            #start a while loop for the second index to be searched
            for index_2 in range(len(nums)):
                #make sure not to reuse the same first index for the second index as well.
                if index_2 == index_1:
                    continue
                #start a while loop for the third index to be searched
                for index_3 in range(len(nums)):
                    #make sure not to reuse the first and second indexes for the third index.
                    if index_3 == index_1 or index_3 == index_2:
                        continue
                    #print("Index1=%d,index2=%d,index3=%d\n" %(index_1,index_2,index_3))
                    #Once you found the three variables that add up to 0 make sure not to add a duplicate entry into return_list.
                    if nums[index_1] + nums[index_2] + nums[index_3] == 0:
                        #print("Newly found values(%d,%d,%d) are at location(%d,%d,%d)\n" \
                        #%(array[index_1],array[index_2],array[index_3],index_1,index_2,index_3))
                        #start iterating the lists contained in return list
                        match_found = False
                        new_list = []
                        new_list.append(nums[index_1])
                        new_list.append(nums[index_2])
                        new_list.append(nums[index_3])
                        #print(new_list)

                        if return_list == None:
                            #add the new list to the empty return list.
                            return_list.append(new_list)
                        else:
                            for list in return_list:
                                #check if the list elements match with the new list to be added.
                                #print("list(%d:%d:%d) newlist(%d:%d:%d)\n" %(list[0],list[1],list[2],new_list[0],new_list[1],new_list[2]))
                                location1=-1
                                location2=-1
                                location3=-1
                                for index_new_list in range(len(new_list)):
                                    for index_return_list in range(len(list)):
                                        if new_list[index_new_list] == list[index_return_list]:
                                            if location1 == -1:
                                                location1=index_return_list
                                                break
                                            elif location2 == -1 and index_return_list != location1:
                                                location2= index_return_list
                                                break
                                            elif location3 == -1 and index_return_list != location1 and index_return_list != location2:
                                                location3 = index_return_list
                                                break
                                if location1 != -1 and location2 != -1 and location3 != -1:
                                    match_found = True
                                    break
                        #do not add this list if item_match is true.
                        if match_found == False:
                            return_list.append(new_list)
                            #print("Append new_list to original return list.\n")
                            #print(new_list)
        #print(return_list)
        return return_list

sol = Solution()
#array=[-1, 0, 1, 2, -1, -4]
array=[0,3,0,1,1,-1,-5,-5,3,-3,-3,0]
print(sol.threeSum(array))
