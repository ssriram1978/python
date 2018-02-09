class minheap:
    def __init__(self):
        self.head=None
        self.minheap_array=[]

    def add(self,item):
        #add an item to the heap
        #add it to the end of the list and invoke heapifyUp
        self.minheap_array.append(item)
        self.heapifyUp()

    def print_minHeap(self):
        print(self.minheap_array)

    def swap(self,index1,index2):
        if index1 < 0 or index1 > len(self.minheap_array):
            return
        if index2 < 0 or index2 > len(self.minheap_array):
            return
        temp=self.minheap_array[index1]
        self.minheap_array[index1]=self.minheap_array[index2]
        self.minheap_array[index2]=temp

    def heapifyUp(self):
        #take the last item and bubble it up to the right location
        item_to_be_heapified_index=len(self.minheap_array)-1
        while self.hasParent(item_to_be_heapified_index):
            item_to_be_heapified = self.minheap_array[item_to_be_heapified_index]
            if self.getParentNode(item_to_be_heapified_index) > item_to_be_heapified:
                #swap the elements
                self.swap(item_to_be_heapified_index,self.getParentIndex(item_to_be_heapified_index))
                item_to_be_heapified_index=self.getParentIndex(item_to_be_heapified_index)
            else:
                break

    def heapifyDown(self):
        #swap the bottom element to the top of the node
        #find the smallest among the three (parent, leftchild, rightchild) and swap the element in such a way
        #that the smallest node stays on top and the largest node moves down
        self.swap(len(self.minheap_array)-1,0)
        minIndex=0
        while minIndex < len(self.minheap_array)-1:
            #find the smallest among the three (parent, leftchild, rightchild)
            if self.hasLeftChild(minIndex):
                minofTwo=self.getLeftChildIndex(minIndex)

                if self.hasRightChild(minIndex):
                    rightChild_val=self.getRightChildNode(minIndex)
                    if self.minheap_array[minofTwo] > rightChild_val:
                        minofTwo=self.getRightChildNode(minIndex)

                if self.minheap_array[minofTwo] < self.minheap_array[minIndex]:
                    self.swap(minofTwo,minIndex)
                    minIndex=minofTwo
                else:
                    break
            else:
                break

    def delete(self,item):
        #delete an item from the heap
        #pop the last item from the list and overwrite this item from the list
        #invoke heapifyDown to move the item to the correct location.
        return None

    def getParentIndex(self,index):
        # parent node = current index - 1 /2
        return (index-1)//2

    def getLeftChildIndex(self,index):
        #child node = current index * 2 + 1
        return (index*2) + 1

    def getRightChildIndex(self, index):
        # child node = current index * 2 + 2
        return (index * 2) + 2

    def hasLeftChild(self, index):
        # child node = current index * 2 + 1
        index = self.getLeftChildIndex(index)
        if index >=0 and index <len(self.minheap_array):
            return True
        else:
            return False

    def hasRightChild(self, index):
        # child node = current index * 2 + 1
        index = self.getRightChildIndex(index)
        if index >= 0 and index < len(self.minheap_array):
            return True
        else:
            return False

    def hasParent(self, index):
        index = self.getParentIndex(index)
        if index >= 0 and index < len(self.minheap_array):
            return True
        else:
            return False

    def getParentNode(self, index):
        # parent node = current index - 1 /2
        if index <= 0 or index > len(self.minheap_array):
            return None
        return self.minheap_array[self.getParentIndex(index)]


    def getLeftChildNode(self, index):
        if index < 0 or index > len(self.minheap_array):
            return None
        return self.minheap_array[self.getLeftChildIndex(index)]


    def getRightChildNode(self, index):
        if index < 0 or index > len(self.minheap_array):
            return None
        return self.minheap_array[self.getRightChildIndex(index)]

    def getHeapSize(self):
        return len(self.minheap_array)

minheap_obj=minheap()
minheap_obj.add(5)
minheap_obj.add(3)
minheap_obj.print_minHeap()
minheap_obj.add(8)
minheap_obj.print_minHeap()
minheap_obj.add(12)
minheap_obj.print_minHeap()
minheap_obj.add(1)
minheap_obj.print_minHeap()

for index in range(minheap_obj.getHeapSize()):
    minheap_obj.heapifyDown()
    minheap_obj.print_minHeap()
