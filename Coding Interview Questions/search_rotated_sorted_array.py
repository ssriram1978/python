"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

"""
1. First find the pivot point.
    In order to find the pivot point, perform a binary search with the following condition:
2. Perform Binary search on the left array of the pivot.
3. Perform Binary search on the right array of the pivot.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """