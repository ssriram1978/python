"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""

"""
Algorithm:
----------
Create an empty output list.
start=0
end=len(input)
while start < end:
    Create a string with input[start] appended to it followed by -> sign.
    while the next element input[start+1] in the list differ with the current element input[start] by 1,
        keep incrementing the start index.
    Append the input[start] to the string and append the string to the output list.
return output list
"""
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output_list=[]
        start=0
        end=len(nums)
        #outer while loop iterates while start is less than end
        while start < end:
            #store the first element in the string
            string=str(nums[start])
            #increment the index by 1
            start+=1
            #declare a bool to check if you found a range
            found_a_range=False
            #iterate over the elements if you find them contiguous.
            while start < end:
                #keep moving start as long as the elements are contiguous.
                if nums[start] - nums[start-1] == 1:
                    found_a_range=True
                    start+=1
                else:
                    break
            #if you found a range, then, append it to the string
            if found_a_range == True:
                #append the end of the range to the string
                string+="->"+str(nums[start-1])
            #finally append the string to the output list
            output_list.append(string)

        return output_list

sol=Solution()
list=[0,1,2,4,5,7]
print(sol.summaryRanges(list))
list=[0,3]
print(sol.summaryRanges(list))