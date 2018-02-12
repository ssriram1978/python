"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
"""
In the first sweep, compute min and max and also keep adding the elements to a hash table. o(n)
Having computed min and max, now start a for loop and check if the index is there in the hash table, if it is not
there in the hash table, then, append this index to the output list.o(x) where x is the range.
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """