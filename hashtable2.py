
class Node:
    def __init__(self, hash, key, object):
        self.__used = 1
        self.__hash=hash
        self.__key=key
        self.__object = object
        #print("\nAdding key=%d"%(key) + " object=%d" %(object))

    def match_node(self,key):
        if(self.__key==key):
            #print("\nFound a match for this key(%d)" % (key) + "hash=%d" % (self.__hash) + "object=%d" % (self.__object))
            return self.__object
        else:
            print("\nNo match found for key(%d)" % (key) + "hash=%d" % (self.__hash) + "object=%d" % (self.__object))
            return None

    # staticmethod
    def print_node(self, node):
        if (node == None):
            return
        #print("node.__used=%d" % (node.__used) + "node.__object=%d"%(node.__object) + "node.__key=%d"%(node.__key) + "node.__hash=%d"%(node.__hash))

class hash_array:
    def __init__(self, tableindex):
        #use a dictionary instead of list
        self.__hash_linked_list = {}
        self.__row=tableindex

    def get_row(self):
        return self.__row

    def get_list(self):
        return self.__hash_linked_list

    def print_list(self):
        print(self.__hash_linked_list)

    def search_for_node(self,key):
        node=self.__hash_linked_list[key]
        if(node == None):
            print("No node found.")
            return None
        else:
            return node

    def return_list_at_location(self, index):
        node=self.__hash_linked_list[key]
        if(node == None):
            print("No node found.")
            return None
        else:
            return node

    def add_node_to_list(self, key,object):
        self.__hash_linked_list[key]=Node(self.__row,key,object)

class hashtable:
    __USED=1
    __NOT_USED=2

    def __init__(self, tablesize):
            self.__tablesize = tablesize
            print("tablesize=%d"%(self.__tablesize))
            #use a dictionary instead of list.
            self.__hash_array = {}
            for i in range(tablesize):
                self.__hash_array[i]=hash_array(i)

    def return_node_at_location(self,index):
        hash = self.generate_hash_key(index)
        return self.__hash_array[hash]

    def search_using_key_in_hashtable(self,key):
        hash=self.generate_hash_key(key)
        row=self.__hash_array[hash]
        if(row != None):
            #print("\nFound the row, searching for the node with key=%d"%(key))
            node=row.search_for_node(key)
            if(node != None):
                print("\nFound a match for this key(%d)" % (key))

    def generate_hash_key(self,key):
        return key % self.__tablesize

    def get_length(self):
        return self.__hash_array.__sizeof__()

    def add_to_hash_table(self,key,object):
        hash = self.generate_hash_key(key)
        node=self.__hash_array[hash]
        if node == None:
            #print("Empty node at key %d"%(key))
            return
        node.add_node_to_list(key,object)

HASH_TABLE_SIZE=10
MAX_ELEMENTS=10000
hashtable_obj=hashtable(HASH_TABLE_SIZE)
print(hashtable_obj.get_length())

for index in range(MAX_ELEMENTS):
    hashtable_obj.add_to_hash_table(index,index)

for index in range(MAX_ELEMENTS):
    row_obj=hashtable_obj.return_node_at_location(index)
    #if(row_obj != None):
    #    object = row_obj.print_list()

for index in range(MAX_ELEMENTS):
    obj=hashtable_obj.search_using_key_in_hashtable(index)
    #if(obj != None):
    #    print(obj.print_node(obj))

#hashtable2 = {}
#hashtable2.items()
#print(len(hashtable2()))

