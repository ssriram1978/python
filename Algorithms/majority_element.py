"""
Majority Element is an element that makes up more than half of the items in the array.
Given positive integers array, find the majority element.
If there is no majority element, return -1.
Do this O(N) time and O(1) space.
Input: 1 2 5 9 5 9 5 5 5
Output: 5
"""

class Solution:
    def getCandidate(self,array):
        majority=0
        count=0
        for n in array:
            if count==0:
                print("Setting %d as majority"%(n))
                majority=n
            if n == majority:
                count+=1
            else:
                count-=1
        return majority
    def validate(self,array,majority):
        count=0
        for n in array:
            if n == majority:
                count+=1
        if count > len(array)//2:
            return count
        else:
            return -1
    def findMajorityElement(self,array):
        candidate=self.getCandidate(array)
        return self.validate(array,candidate)

sol=Solution()
array=[1,2,5,1]
print(sol.findMajorityElement(array))