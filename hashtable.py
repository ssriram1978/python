
class Node:
    def __init__(self, key, object):
        self.__used = 1
        self.__key=key
        self.__object = object
        print("\nAdding key=%d"%(key) + " object=%d" %(object))

    def match_node(self,key):
        if(self.__key==key):
            print("\nFound a match for this key(%d)" % (key) + "object=%d" % (self.__object))
            return self.__object
        else:
            return None

    # staticmethod
    def print_node(self, node):
        if (node == None):
            return
        print("node.__used=%d" % (node.__used) + "node.__object=%d"%(node.__object) + "node.__key=%d"%(node.__key))

class hash_array:
    def __init__(self, tableindex):
        self.__hash_linked_list = []
        self.__row=tableindex

    def get_row(self):
        return self.__row

    def get_list(self):
        return self.__hash_linked_list

    def print_list(self):
        for node in self.__hash_linked_list:
            print node.print_node(node)

    def search_for_node(self,key):
        for node in self.__hash_linked_list:
            object=node.match_node(key)
            if(object != None):
                print("Match found")
                return object
        return None

    def return_list_at_location(self, index):
        if (len(self.__hash_linked_list) == 0):
            return None
        else:
            try:
                obj = self.__hash_linked_list[index]
                return obj
            except IndexError:
                return None

    def add_node_to_list(self, key,object):
        self.__hash_linked_list.append(Node(key,object))

class hashtable:
    __USED=1
    __NOT_USED=2

    def __init__(self, tablesize):
            self.__tablesize = tablesize
            print("tablesize=%d"%(self.__tablesize))
            self.__hash_array = []
            for i in range(tablesize):
                self.__hash_array.append(hash_array(i))

    def return_node_at_location(self,index):
        return self.__hash_array[index]

    def search_using_key_in_hashtable(self,key):
        row=self.__hash_array[key]
        if(row != None):
            print("\nFound the row, searching for the node with key=%d"%(key))
            node=row.search_for_node(key)
            if(node != None):
                print("\nFound a match for this key(%d)" % (key))

    def generate_hash_key(self,key):
        return key % self.__tablesize

    def get_length(self):
        return self.__hash_array.__sizeof__()

    def add_to_hash_table(self,key,object):
        node=self.__hash_array[key]
        if node == None:
            print("Empty node at key %d"%(key))
            return
        node.add_node_to_list(key,object)

MAX_ELEMENTS=10
hashtable_obj=hashtable(MAX_ELEMENTS)
print(hashtable_obj.get_length())

for index in range(20):
    hashtable_obj.add_to_hash_table(hashtable_obj.generate_hash_key(index),index)

for index in range(20):
    row_obj=hashtable_obj.return_node_at_location(index)
    if(row_obj != None):
        object = row_obj.print_list()

    for index in range(20):
        obj=hashtable_obj.search_using_key_in_hashtable(hashtable_obj.generate_hash_key(index))
        if(obj != None):
            print(obj.print_node(node))

#hashtable2 = {}
#hashtable2.items()
#print(len(hashtable2()))

