class Node :
    def __init__(self,object,left=None,right=None):
        self.__object=object
        self.__left=left
        self.__right=right

    def get_object(self):
        return self.__object

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self,node):
        self.__left=node

    def set_right(self,node):
        self.__right=node

class Binary_tree :
    def __init__(self):
        self.__btree=None

    def get_btree_root(self):
        return self.__btree

    def add_node_to_btree(self,node,object):
        if object == None:
            return None

        if node == None:
            node2 = Node(object)
            if self.__btree == None:
                self.__btree = node2
            return node2

        if (node.get_object() <= object):
            node.set_right(self.add_node_to_btree(node.get_right(), object))
        else:
            node.set_left(self.add_node_to_btree(node.get_left(), object))
        return node

    def print_binary_tree_inorder(self,node):
        if(node == None):
            return
        else:
            self.print_binary_tree_inorder(node.get_left())
            print(node.get_object())
            self.print_binary_tree_inorder(node.get_right())

btree = Binary_tree()
btree.add_node_to_btree(btree.get_btree_root(),4)
btree.add_node_to_btree(btree.get_btree_root(),8)
btree.add_node_to_btree(btree.get_btree_root(),3)
btree.add_node_to_btree(btree.get_btree_root(),5)
btree.add_node_to_btree(btree.get_btree_root(),1)
btree.add_node_to_btree(btree.get_btree_root(),9)

btree.print_binary_tree_inorder(btree.get_btree_root())


