"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
"""
Algorithm:
----------
The problem was posed with three colours, here `0′, `1′ and `2′. The array is divided into four sections:

a[1..Lo-1] zeroes (red)
a[Lo..Mid-] ones (white)
a[Mid..Hi] unknown
a[Hi+1..N] twos (blue)
The unknown region is shrunk while maintaining these conditions

Lo := 1; Mid := 1; Hi := N;
while Mid <= Hi do
Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and a[Hi+1..N]=2; a[Mid..Hi] are unknown.
case a[Mid] in
0: swap a[Lo] and a[Mid]; Lo++; Mid++
1: Mid++
2: swap a[Mid] and a[Hi]; Hi–
— Dutch National Flag Algorithm, or 3-way Partitioning —
"""

class Solution(object):
    def swap(self,array,index1,index2):
        temp=array[index1]
        array[index1]=array[index2]
        array[index2]=temp

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0:
            return

        low=0
        mid=0
        high=len(nums)-1

        while mid < high:
            if nums[mid] == 0:
                #swap it with low
                self.swap(nums,mid,low)
                low+=1
                mid+=1
            elif nums[mid] == 1:
                #let it remain in the same place
                mid+=1
            elif nums[mid] == 2:
                #swap high with mid
                self.swap(nums,high,mid)
                high-=1

sol=Solution()
nums=[0,2,1,1,2,2,2,2,2,2]
sol.sortColors(nums)
print(nums)