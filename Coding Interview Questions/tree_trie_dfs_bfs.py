from collections import defaultdict
from collections import deque
class singlyLinkedListNode:
    def __init__(self,value):
        self.value=value
        self.next=None

class singlyLinkedList:
    def __init__(self):
        self.head=None
    def add_node(self,value):
        if self.head==None:
            self.head=singlyLinkedListNode(value)
        else:
            currentNode=self.head
            while currentNode.next != None:
                currentNode=currentNode.next
            currentNode.next=singlyLinkedListNode(value)
    def printSinglyLinkedList(self):
        current=self.head
        while current != None:
            print("%d -->"%(current.value),end=" ")
            current=current.next
        print("\n")
    def reverseSinglyLinkedList(self):
        if self.head == None:
            return
        previous=None
        current=self.head
        next=None
        while current != None:
            if current.next==None:
                self.head=current
            next=current.next
            current.next=previous
            previous=current
            current=next

singlyList=singlyLinkedList()
for index in range(10):
    singlyList.add_node(index)
print("Singly linked list = " + str(singlyList.printSinglyLinkedList()))
singlyList.reverseSinglyLinkedList()
print("Reversed Singly Linked list = " + str(singlyList.printSinglyLinkedList()))

class Node:
    def __init__(self,value):
        self.value=value
        self.leftNode=None
        self.rightNode=None
class BST:
    def __init__(self):
        self.head=None
    def printBST(self):
        self.printBSTRecurse(self.head)
        print("\n")
    def printBSTRecurse(self,node):
        if node==None:
            return
        self.printBSTRecurse(node.leftNode)
        print("%d"%(node.value),end=" ")
        self.printBSTRecurse(node.rightNode)
    def recurseAddNode(self,node,value):
        if node==None:
            return Node(value)
        if value > node.value:
            node.rightNode = self.recurseAddNode(node.rightNode,value)
        elif value <= node.value:
            node.leftNode = self.recurseAddNode(node.leftNode,value)
        return node
    def addNode(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            self.head=self.recurseAddNode(self.head,value)
    def printPreorderRecurse(self,node):
        if node==None:
            print("None ",end="")
            return
        print("%d "%(node.value),end="")
        self.printPreorderRecurse(node.leftNode)
        self.printPreorderRecurse(node.rightNode)
    def printPreorder(self):
        self.printPreorderRecurse(self.head)
        print("\n")
    def searchNodePath(self,value,alg):
        output=[]
        nodeTraversed=defaultdict(int)
        if self.head==None:
            return output
        if alg=="DFS":
            output=self.DFS(self.head,value,nodeTraversed)
        elif alg=="BFS":
            output=self.BFS(self.head,value,nodeTraversed)
        print("Node traversed="+str(nodeTraversed))
        return output
    def DFS(self,node,value,traversedNodes):
        output = []
        if node==None:
            return output
        if node.value == value:
            traversedNodes[node.value]=1
            print("DFS: Found the node %d" %(node.value))
            output.append(node.value)
        elif traversedNodes[node.value]==0:
            traversedNodes[node.value]=1
            returned_output=self.DFS(node.leftNode,value,traversedNodes)
            if returned_output!=[]:
                output+=returned_output
            else:
                returned_output = self.DFS(node.rightNode, value, traversedNodes)
                if returned_output!=[]:
                    output+=returned_output
        return output

    def BFS(self,node,value,traversedNodes):
        output = []
        isFound=False
        if node==None:
            return output
        queue=deque()
        traversedNodes[node.value]=1
        queue.append(node)
        while isFound==False and len(queue) > 0:
            node=queue.popleft()
            output.append(node.value)
            if node.value==value:
                isFound=True
                print("BFS: Found the node %d"%(node.value))
                break
            else:
                if node.leftNode != None and traversedNodes[node.leftNode.value]==0:
                    queue.append(node.leftNode)
                    traversedNodes[node.leftNode.value]=1
                if node.rightNode != None and traversedNodes[node.rightNode.value]==0:
                    queue.append(node.rightNode)
                    traversedNodes[node.rightNode.value]=1
        if isFound==True:
            return output
        else:
            return -1

bst=BST()
bst.addNode(5)
bst.addNode(9)
bst.addNode(8)
bst.addNode(6)
bst.addNode(10)
bst.addNode(3)
bst.addNode(4)
bst.addNode(2)
bst.addNode(1)
bst.addNode(0)

print("in order walk returned " + str(bst.printBST()))
print("preorder walk returned" +  str(bst.printPreorder()))
print("BFS search for %d returned" %(9) + str(bst.searchNodePath(9,"BFS")))
print("DFS search for %d returned" %(9) + str(bst.searchNodePath(9,"DFS")))

class TrieNode:
    def __init__(self):
        self.neighbors=[0]*26
        self.end_of_word=False

class Trie:
    def __init__(self):
        self.head=TrieNode()
    def getCharIndex(self,character):
        ascii_char=ord(character)
        if ascii_char >= ord('a') and ascii_char <= ord('z'):
            return ascii_char-ord('a')
        else:
            return -1
    def addWord(self,word):
        currNode=self.head
        for character in word:
            ascii_char_index=self.getCharIndex(character)
            if currNode[ascii_char_index]==None:
                currNode[ascii_char_index]=TrieNode()
            currNode=currNode[ascii_char_index]
        currNode.end_of_word=True
    def isPrefixFound(self,prefix):
        prefixEndNode=self.getPrefixLocation(prefix)
        if prefixEndNode == None:
            return False
        else:
            return True
    def getPrefixLocation(self,prefix):
        prefixEndNode=None
        currNode = self.head
        for character in prefix:
            ascii_char_index = self.getCharIndex(character)
            if currNode[ascii_char_index] == None:
                return None
            else:
                currNode = currNode[ascii_char_index]
                prefixEndNode = currNode
        return prefixEndNode
    def getRhymingWordsRecurse(self,string,node):
        rhyming_words=[]
        if node == None:
            return rhyming_words
        else:
            for index in range(26):
                word = string
                word+=self.getPrefixLocation(node[index])
                rhyming_words.append(word)
            return rhyming_words
    def getRhymingWords(self,prefix):
        rhyming_words=[]
        currNode = self.head
        if self.isPrefixFound(prefix)==True:
            rhyming_words+=self.getRhymingWordsRecurse(prefix,self.getPrefixLocation(prefix))
        return rhyming_words

trie=Trie()
trie.addWord("sriram")
trie.addWord("sridhar")
trie.addWord("sriya")
trie.addWord("srinivas")
print(trie.getRhymingWords("sri"))
