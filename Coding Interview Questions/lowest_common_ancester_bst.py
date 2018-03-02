"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.

"""
"""
Algorithm:
----------
If we are given a BST where every node has parent pointer, 
then LCA can be easily determined by traversing up using parent pointer and printing the first intersecting node.
We can solve this problem using BST properties. 
We can recursively traverse the BST from root. 
The main idea of the solution is, while traversing from top to bottom, 
                                 the first node n we encounter with value between n1 and n2, 
                                 i.e., n1 < n < n2 or same as one of the n1 or n2, is LCA of n1 and n2 
                                 (assuming that n1 < n2). 
So just recursively traverse the BST in, 
    if node’s value is greater than both n1 and n2 then our LCA lies in left side of the node, 
    if it’s is smaller than both n1 and n2, then LCA lies on right side. 
    Otherwise root is LCA (assuming that both n1 and n2 are present in BST)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
