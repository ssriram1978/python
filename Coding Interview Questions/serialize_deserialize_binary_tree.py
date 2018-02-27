"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.



Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.


"""
"""
For serializing a binrary tree, 
    perform a breadth first search and keep writing the content of the elements into a string and return the string.
For de-serializing a binrary tree, 
    Perform a depth first 
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root=None

    def addNodeToBSTRecurse(self,node,value):
        if node == None:
            return TreeNode(value)
        if value <= node.val:
            node.left=self.addNodeToBSTRecurse(node.left,value)
        else:
            node.right = self.addNodeToBSTRecurse(node.right, value)
        return node

    def addNodeToBST(self, value):
        if self.root == None:
            self.root=TreeNode(value)
            return
        self.root = self.addNodeToBSTRecurse(self.root,value)

    def getHead(self):
        return self.root


    def printBSTInorderRecurse(self,node):
        if node == None:
            return None
        output_list=[]
        left_list=self.printBSTInorderRecurse(node.left)
        if left_list != None:
            output_list.extend(left_list)
        output_list.append(node.val)
        right_list = self.printBSTInorderRecurse(node.right)
        if right_list != None:
            output_list.extend(right_list)
        return output_list

    def printBSTPreorderRecurse(self, node):
        if node == None:
            return None
        output_list = []
        output_list.append(node.val)
        left_list = self.printBSTPreorderRecurse(node.left)
        if left_list != None:
            output_list.extend(left_list)
        right_list = self.printBSTPreorderRecurse(node.right)
        if right_list != None:
            output_list.extend(right_list)
        return output_list

    def printBST(self):
        print(self.printBSTInorderRecurse(self.root))
        print(self.printBSTPreorderRecurse(self.root))


bst=BST()
"""
      9
    /   \
   1     10
  / \   /  \
null 2 null 20
    / \     / \
null   8   11  null
      / \
     3   null
    / \
 null  4
      / \
   null  7
        / \
       5  null
      / \
    null 6
        / \
    null  null
"""

bst.addNodeToBST(9)
bst.addNodeToBST(1)
bst.addNodeToBST(2)
bst.addNodeToBST(8)
bst.addNodeToBST(3)
bst.addNodeToBST(4)
bst.addNodeToBST(7)
bst.addNodeToBST(5)
bst.addNodeToBST(6)
bst.addNodeToBST(10)
bst.addNodeToBST(20)
bst.addNodeToBST(11)

print(bst.printBST())

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return
        serialize_queue=deque()

        output_string=""
        serialize_queue.append(root)
        while len(serialize_queue) > 0:
            #dequeue and process the elements
            node = serialize_queue.popleft()
            if node == None:
                #append null to the output queue.
                output_string+="null" + " "
            else:
                #Append the content of the node to the output queue.
                output_string += str(node.val) + " "
                #enqueue the child nodes to the serialize queue
                serialize_queue.append(node.left)
                serialize_queue.append(node.right)
        return output_string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == None or data == "":
            return
        bst=BST()

        tree_list=data.strip().split()
        for index in range(len(tree_list)):
            if tree_list[index]=="null":
                continue
            else:
                node_val=int(tree_list[index])
                bst.addNodeToBST(node_val)
        return bst

# Your Codec object will be instantiated and called as such:
codec = Codec()
string_tree=codec.serialize(bst.getHead())
print(string_tree)
codec2=Codec()
bst2=codec2.deserialize(string_tree)
print("Deserialized bst="+ codec2.serialize((bst2.getHead())))
#codec.deserialize(codec.serialize(root))