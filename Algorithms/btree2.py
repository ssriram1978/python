class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class btree:
    def __init__(self,array):
        self.root=None
        self.is_binary_tree = 1

        for index in range(len(array)):
            self.construct_btree(self.root,array[index])

    def construct_btree(self,current_node,data):
        if current_node == None:
            new_node=node(data)
            if self.root == None:
                self.root=new_node
            return new_node

        if current_node.data >= data :
            current_node.left = self.construct_btree(current_node.left,data)
        elif current_node.data < data:
            current_node.right = self.construct_btree(current_node.right,data)

        return current_node

    def print_in_order(self,node):
        if node==None:
            return
        self.print_in_order(node.left)
        print("data=%d\n" %(node.data))
        self.print_in_order(node.right)

    def computeBSTHeight(self, root):
        # return 0 if it is a null node.
        if root == None:
            return 0

        # if the tree was already declared as not binary tree
        # return this value to the calling function.
        if self.is_binary_tree == 0:
            return self.is_binary_tree

        # compute the height of left subtree
        left_height = self.computeBSTHeight(root.left)

        # compute the height of right subtree
        right_height = self.computeBSTHeight(root.right)

        # if the tree was already declared as not binary tree
        # return this value to the calling function.
        if self.is_binary_tree == 0:
            return self.is_binary_tree

        # compute the difference between left and right tree height
        if right_height > left_height:
            difference_in_height = right_height - left_height
            height = right_height
        else:
            difference_in_height = left_height - right_height
            height = left_height

        # if height differs more than 1 declare this as not a binary tree
        if difference_in_height > 1:
            self.is_binary_tree = 0

        # compute the height of the current node
        return height + 1


    def checkBST(self,root):
        # return 0 if there are no nodes.
        if root == None:
            return 0

        tree.computeBSTHeight(root)
        return tree.is_binary_tree


array=[5,3,4,2,1,6,7]
tree=btree(array)
tree.print_in_order(tree.root)
print(tree.checkBST(tree.root))

array2=[1,2,3,4,5,6,7,8]
tree2=btree(array2)
tree.print_in_order(tree2.root)
print(tree.checkBST(tree2.root))