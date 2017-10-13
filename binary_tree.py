class Node :
    def __init__(self,object,left=None,right=None):
        self.__object=object
        self.__left=left
        self.__right=right
        self.__height=0

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

    def set_height(self,height):
        self.__height=height

    def get_height(self):
        return self.__height

class Binary_tree :
    def __init__(self):
        self.__btree=None
        self.__btree_balanced=None

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
            print("value=%d and height=%d"%(node.get_object(),node.get_height()))
            self.print_binary_tree_inorder(node.get_right())

    def return_sorted_list_inorder(self,node):
        if(node == None):
            return
        else:
            list=[]
            object = self.return_sorted_list_inorder(node.get_left())

            if(object != None):
                list+=object

            list.append(node.get_object())
            object = self.return_sorted_list_inorder(node.get_right())

            if(object != None):
                list+=object

            return list

    def create_balanced_binary_tree(self,sorted_list,start,end):
        if(start > end):
            return None

        middle=(start+end)//2
        node = Node(sorted_list[middle])
        node.set_left(self.create_balanced_binary_tree(sorted_list, start, middle - 1))
        node.set_right(self.create_balanced_binary_tree(sorted_list, middle + 1, end))
        return node

    def create_balanced_binary_tree_from_sorted_list(self,sorted_list):
        if(sorted_list == None or len(sorted_list)==None):
            return None
        self.__btree_balanced = self.create_balanced_binary_tree(sorted_list,0,len(sorted_list)-1)

    def get_self_balanced_tree_root(self):
        return self.__btree_balanced

    def compute_height_of_binary_tree(self,node=None):
        if(node == None):
            return 0
        height=max(self.compute_height_of_binary_tree(node.get_left()),
                   self.compute_height_of_binary_tree(node.get_right()))+1
        node.set_height(height)
        return height

    def delete_node_from_binary_tree(self,node):
        #to be implemented
        return None

    def rebalance_binary_tree(self,node):
        #to be implemented
        return None

    def get_nodes_that_are_unbalanced(self,node=None):

        if(node == None):
            return None

        unbalanced_nodes = ""
        return_value = self.get_nodes_that_are_unbalanced(node.get_left())

        if return_value != None:
            unbalanced_nodes += return_value

        left_node=node.get_left()
        right_node=node.get_right()

        if(left_node == None and right_node != None and right_node.get_height() > 1):
            unbalanced_nodes += ("\n\ncurrent node value=%d and height=%d\n" % (node.get_object(), node.get_height()))
            unbalanced_nodes += ("right_node value=%d and height=%d\n" %(right_node.get_object(),right_node.get_height()))
        elif(right_node == None and left_node != None and left_node.get_height() > 1):
            unbalanced_nodes += ("\n\ncurrent node value=%d and height=%d\n" % (node.get_object(), node.get_height()))
            unbalanced_nodes += ("left_node value=%d and height=%d\n" %(left_node.get_object(),left_node.get_height()))
        elif(right_node != None and left_node != None and abs(left_node.get_height()-right_node.get_height()) > 1):
            unbalanced_nodes += ("\n\ncurrent node value=%d and height=%d\n" % (node.get_object(), node.get_height()))
            unbalanced_nodes += ("right_node value=%d and height=%d\n"%(right_node.get_object(), right_node.get_height()))
            unbalanced_nodes += ("left_node value=%d and height=%d\n" % (left_node.get_object(), left_node.get_height()))

        return_value = self.get_nodes_that_are_unbalanced(node.get_right())
        if return_value != None:
            unbalanced_nodes += return_value

        return unbalanced_nodes


btree = Binary_tree()
btree.add_node_to_btree(btree.get_btree_root(),4)
btree.add_node_to_btree(btree.get_btree_root(),8)
btree.add_node_to_btree(btree.get_btree_root(),3)
btree.add_node_to_btree(btree.get_btree_root(),5)
btree.add_node_to_btree(btree.get_btree_root(),1)
btree.add_node_to_btree(btree.get_btree_root(),9)
btree.add_node_to_btree(btree.get_btree_root(),10)
btree.add_node_to_btree(btree.get_btree_root(),11)

#btree.print_binary_tree_inorder(btree.get_btree_root())
btree.compute_height_of_binary_tree(btree.get_btree_root())
#return_value=btree.get_nodes_that_are_unbalanced(btree.get_btree_root())
#print(return_value)
#btree.print_binary_tree_inorder(btree.get_btree_root())
sorted_list = btree.return_sorted_list_inorder(btree.get_btree_root())
print(sorted_list)
btree.create_balanced_binary_tree_from_sorted_list(sorted_list)
btree.compute_height_of_binary_tree(btree.get_self_balanced_tree_root())
btree.print_binary_tree_inorder(btree.get_self_balanced_tree_root())
return_value=btree.get_nodes_that_are_unbalanced(btree.get_btree_root())
print("get_nodes_that_are_unbalanced for unbalanced btree returned" + return_value)
return_value=btree.get_nodes_that_are_unbalanced(btree.get_self_balanced_tree_root())
print("get_nodes_that_are_unbalanced for balanced btree returned" + return_value)
