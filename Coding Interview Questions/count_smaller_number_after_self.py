"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].


"""
"""
1. Brute force: Use two for loops. o(n**2)
Use two loops. The outer loop picks all elements from left to right. 
The inner loop iterates through all the elements on right side of the picked element and updates countSmaller[].

2. AVL tree: o(nlogn)
A Self Balancing Binary Search Tree (AVL, Red Black,.. etc) can be used to get the solution in O(nLogn) time complexity.
We can augment these trees so that every node N contains size the subtree rooted with N.
We have used AVL tree in the following implementation.
We traverse the array from right to left and insert all elements one by one in an AVL tree.
While inserting a new key in an AVL tree, we first compare the key with root.
If key is greater than root, then it is greater than all the nodes in left subtree of root.
So we add the size of left subtree to the count of smaller element for the key being inserted.
We recursively follow the same approach for all nodes down the root.
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
