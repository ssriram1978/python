"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
"""
1. Sort the numbers in the order of O(nlogn) HEAP sort, Quick(pivot) sort - in place O(1)space complexity or
    Use mergesort O(n) space complexity.
2. Directly index into the sorted array at the given index and return the value. O(1)
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
