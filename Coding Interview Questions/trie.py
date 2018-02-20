"""
A Trie is a special tree which stores words and sentences.
Unlike Linked lists and trees, each node does not explicitly store a character in it.
The root node is an array of 26 contiguous nodes called neighbors which are indexed from 0-26.
index 0 implicitly means character 'a'
index 25 implicitly is character 'z'.
When you access these neighbors, and if they are not Null, it implicitly means that that character is present.
Note that each neighbor recursively points to 26 more nodes.
Trie is used to store a bunch of dictionary words and is easier to lookup and fetch words rhyming to the original word.
(Just like Google search).
Inserting a word algorithm goes like this:
    Start from root node which has 26 indexes.
    For Every character of the word, do the following:
        Compute the ascii value of the character and subtract it from the ascii value of 'a' to get the offset.
        Index directly into the neighbors of the root node at this offset.
        If the content found at the index is not null:
            Search for the next character from the word from this current node.
        Else:
            Create a new node object at the current node location.

Find Rhyming words with the given prefix algorithm goes like this:
    Start from root node which has 26 indexes.
    Declare an empty list which would be used to fetch all the words with the provided prefix.
    For Every character of the prefix, do the following:
        Compute the ascii value of the character and subtract it from the ascii value of 'a' to get the offset.
        Index directly into the neighbors of the root node at this offset.
        If the content found at the index is not null:
            Search for the next character from the word from this current node.
        Else:
            Return empty list
    Once you reached the end of the word, you would break from the for loop.
    The current node points to the node that ends with the prefix.
    Starting from this current node,
        perform a Depth First Search to find all possible words
        append the prefix to these words
        return the list with all possible words back to the calling function.
"""

class Node:
    def __init__(self):
        self.neighbors=[None]*26
        #self.end_of_word=False
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        self.total_number_of_words=0

    def char_to_index(self,char):
        return ord(char)-ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word == None or len(word) == 0:
            return

        # convert to lower case.
        word=word.lower()

        #declare a temp var named as current neighbor
        current_neighbor = self.root
        for index in range(len(word)):
            ascii_of_char=self.char_to_index(word[index])
            if ascii_of_char >= 0 and ascii_of_char <= 26:
                #find if there is already a character existing in the trie
                if current_neighbor != None and current_neighbor.neighbors[ascii_of_char] != None:
                    #you already have one character match
                    #proceed to the next character in the input string
                    # make sure to move the current neighbor accordingly so that the search starts from here.
                    current_neighbor = current_neighbor.neighbors[ascii_of_char]
                    continue
                elif current_neighbor.neighbors[ascii_of_char] == None:
                    #create a new node at this location
                    #print("Adding new node for char %c"%(word[index]))
                    current_neighbor.neighbors[ascii_of_char] = Node()
                    # make sure to move the current neighbor accordingly so that the search starts from here.
                    current_neighbor = current_neighbor.neighbors[ascii_of_char]
            else:
                #invalid characters
                continue

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word == None or len(word) == 0:
            return False

        #convert to lower case.
        word = word.lower()

        # declare a temp var named as current neighbor
        current_neighbor = self.root
        match_found=True
        for index in range(len(word)):
            ascii_of_char = self.char_to_index(word[index])
            if ascii_of_char >= 0 and ascii_of_char <= 26:
                if current_neighbor.neighbors[ascii_of_char] == None:
                    match_found=False
                    break
                else:
                    #print("Match found for character %c" %(word[index]))
                    current_neighbor=current_neighbor.neighbors[ascii_of_char]

        if match_found==True:
            return True
        else:
            return False

    def convert_index_to_char(self, index):
        character=chr(ord('a')+index)
        return character

    def rest_of_the_word(self, startingNode):
        list_of_words=[]
        if startingNode == None:
            return None
        #Perform a DFS (Depth First Search) for each and every character
        for index in range(26):
            if startingNode.neighbors[index] == None:
                continue
            else:
                #print("Found a char %c"%(self.convert_index_to_char(index)))
                current_list = self.rest_of_the_word(startingNode.neighbors[index])
                if current_list != None and current_list != []:
                    for words in current_list:
                        list_of_words.append(self.convert_index_to_char(index)+words)
                else:
                    #print("Appending char %c to list of words"%(self.convert_index_to_char(index)))
                    list_of_words.append(self.convert_index_to_char(index))

        return list_of_words

    def fetch_the_rest_of_the_word(self, prefix):
        if prefix == None or len(prefix) == 0:
            return False

        # convert to lower case.
        prefix=prefix.lower()

        # declare a temp var named as current neighbor
        current_neighbor = self.root

        for index in range(len(prefix)):
            ascii_of_char = self.char_to_index(prefix[index])
            if ascii_of_char >= 0 and ascii_of_char <= 26:
                if current_neighbor.neighbors[ascii_of_char] == None:
                    return False
                else:
                    current_neighbor = current_neighbor.neighbors[ascii_of_char]

        #now that you found the prefix exist in the trie, compose a list of all possible strings with this prefix
        #Perform a DFS (Depth First Search to get the whole sentence and then move on to the next sentence).
        list_of_possible_words = self.rest_of_the_word(current_neighbor)
        for index in range(len(list_of_possible_words)):
            list_of_possible_words[index]= prefix + list_of_possible_words[index]
        return list_of_possible_words

#Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("sriram")
obj.insert("sridhar")
obj.insert("srinivas")
obj.insert("sriya")
param_2 = obj.search("srir")
print(param_2)
print(obj.fetch_the_rest_of_the_word("sri"))
