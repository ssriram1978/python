class hashtable:
    __USED=1
    __NOT_USED=2
    class hash_array:
        class Node:
            def __init__(self,node):
                self.__used = 1
                self.__object=node
                self.__next=None

            #staticmethod
            def print_node(self,node):
                if(node == None):
                    return
                print("node.__used=%d"%(node.__used))
                #print("node.__index=%d"%(node.__index))

        def __init__(self, tableindex):
            self.__hash_linked_list = []

        def return_list_at_location(self,index):
            if(len(self.__hash_linked_list)==0):
                return None
            else:
                try:
                    obj= self.__hash_linked_list[index]
                except IndexError:
                    return None

        def add_node_to_list(self,node):
            self.__hash_linked_list.append(self.Node(node))

    def __init__(self, tablesize):
            self.__tablesize = tablesize
            print("tablesize=%d"%(self.__tablesize))
            self.__hash_array = []
            for i in range(tablesize-1):
                self.__hash_array.append(self.hash_array(i))

    def return_node_at_location(self,index):
        return self.__hash_array[index]

    def generate_hash_key(self,key):
        return key % self.__tablesize

    def get_length(self):
        return self.__hash_array.__sizeof__()

    def add_to_hash_table(self,index,object):
        node=self.__hash_array[index]
        if node == None:
            print("Empty node at location %d"%(index))
            return
        #print(node)

        #list=node.return_list_at_location(0)
        #print(list)
        node.add_node_to_list(object)

        list =node.return_list_at_location(1)

        if list == None:
            print("Empty list at location %d" % (index))
            return

        hashtable.hash_array.Node.print_node(list)

            #if list.__used == 2 :
        #    print("adding a node at index %d"%(index))
        #    list.__used = 1
        #    list.__index=index
        #    list.__object=object
        #else:
        #    print("Performing a linked list search at index %d" % (index))



hashtable_obj=hashtable(20)
print(hashtable_obj.get_length())
for index in range(1,19,1):
    hashtable_obj.add_to_hash_table(hashtable_obj.generate_hash_key(index),index)


#hashtable2 = {}
#hashtable2.items()
#print(len(hashtable2()))

