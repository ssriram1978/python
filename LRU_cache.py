"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
Follow up:
Could you do both operations in O(1) time complexity?
Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

#class LRUCache:
#    def __init__(self, capacity):
#        """
#        :type capacity: int
#        """

#    def get(self, key):
#        """
#        :type key: int
#        :rtype: int
#        """

#    def put(self, key, value):
#       """
#        :type key: int
#        :type value: int
#        :rtype: void
#        """


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


from collections import defaultdict
from collections import deque

class LRUCache:
    capacity = 0
    hashtable = {}
    key_list = deque()
    current_capacity = 0

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity > 0:
            self.capacity = capacity
        self.current_capacity = 0
        # define default dictionary
        self.hashtable = defaultdict(int)

    def print_lru_cache(self):
        print(self.key_list)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return_value = -1

        value = self.hashtable[key]

        if value == 0:
            print("Couldn't find the key(%d) in the dictionary.\n" % (key))
        else:
            # value of the key is found
            #print("For key=%d, got value=%d.\n" % (key, value))
            return_value = value
            # remove this key from the key_list
            self.key_list.remove(key)
            # add this key to the top of the LRU key_list
            self.key_list.append(key)
            #print("Removing key=%d from the keylist and adding it to the front of the list.\n" % (key))

        return return_value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # check for duplicate key
        lookup_value = self.hashtable[key]
        if lookup_value == 0:
            # its a new element, check if the stack reached its capacity.
            if self.current_capacity < self.capacity:
                # increment the current capacity by 1
                self.current_capacity += 1
                # print("Adding key=%d,value=%d to the dictionary and to the front of the key_list.\n"%(key,value))
            else:
                # remove the Least used node
                lru_key = self.key_list.popleft()
                #print("To add key=%d,deleting the least recently used key=%d from key_list and hash table.\n" % (
                #key, lru_key))
                # use this key and delete the node in the dictionary
                del self.hashtable[lru_key]
        else:
            # remove this key from the key_list.
            self.key_list.remove(key)
            #print("Removing key=%d in the key_list and from the hash table.\n"%(key))

        # move this entry to the top of the stack
        self.key_list.append(key)
        # insert the value in the hash table.
        self.hashtable[key] = value
        #print("Inserting key=%d,value=%d in the stack and in the hash table.\n" % (key, value))




# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.print_lru_cache()
obj.put(1, 1)
obj.print_lru_cache()
obj.put(2, 2)
obj.print_lru_cache()
obj.get(1)
obj.print_lru_cache()
obj.put(3, 3)
obj.print_lru_cache()
obj.get(2)
obj.print_lru_cache()
obj.put(4, 4)
obj.print_lru_cache()
obj.get(1)
obj.print_lru_cache()
obj.get(3)
obj.print_lru_cache()
obj.get(4)
obj.print_lru_cache()
"""
operations_list=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
value_list=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
for index in range(len(operations_list)):
    if operations_list[index] == "put":
        val_list=value_list[index]
        obj.put(val_list[0], val_list[1])
    elif operations_list[index] == "get":
        val_list = value_list[index]
        print("Get key=%d returned=%d.\n"%(val_list[0],obj.get(val_list[0])))
"""