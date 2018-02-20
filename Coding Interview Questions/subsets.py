"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
"""
Algorithm:
----------
Perform a Depth First search and whenever you find a possible solution, 
just keep appending it to a list and return the list and return the final
list to the caller.
"""


class Solution(object):
    def create_subsets(self,nums,start,end):
        #base condition
        if start > end:
            return []
        elif start==end:
            return [nums[start]]
        else:
            subset=[[nums[start]]]
            object=self.create_subsets(nums,start+1,end)
            print("object="+str(object))
            if type(object) == list:
                #check if the list has sublists
                if type(object[0]) == list:
                    #append all the elements to the subset
                    for sublist in object:
                        subset.append(sublist)
                    #for every sublist in the list, insert nums[start] at index 0.
                    for sub_object in object:
                        newlist = [nums[start]]
                        for x in sub_object:
                            newlist.append(x)
                        # insert the modified object into the subset
                        subset.append(newlist)
                else:
                    # append all the elements to the subset
                    subset.append(object)
                    newlist=[nums[start]]
                    for x in object:
                        newlist.append(x)
                    # insert the modified object into the subset
                    subset.append(newlist)

            return subset

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) == 0:
            return None

        return self.create_subsets(nums,0,len(nums)-1)

sol=Solution()
nums = [1,2,3,4,5]
output=sol.subsets(nums)
print(output)
print(len(output))