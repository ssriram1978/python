class binary_heap:
    def __init__(self,list):
        self.__capacity=len(list)
        self.__count=len(list)
        self.__heap_arr=[]
        self.__heap_arr.extend(list)

    def parent(self,index):
        if(index < 0 or index > self.__count):
            return -1
        else:
            value = 2 * index + 1
        if (value > self.__count):
            return -1
        else:
            return value

    def leftNode(self,index):
        if (index < 0 or index > self.__count):
            return -1
        else:
            value=2*index + 1
        if (value > self.__count):
            return -1
        else:
            return value

    def rightNode(self, index):
        if (index < 0 or index > self.__count):
            return -1
        else:
            value = 2 * index + 1
        if (value > self.__count):
            return -1
        else:
            return value

    def getCount(self):
        return self.__count

    def getMax(self):
        if(self.__count==0):
            return -1
        else:
            return self.__heap_arr[0]

    def printHeap(self):
        print("count=%d" %(self.__count))
        print(self.__heap_arr)

    def percolateDown(self,index):

        left=self.leftNode(index)
        right=self.rightNode(index)

        print("index2=%d " % (index))
        print("left=%d " % (left))
        print("right=%d " % (right))

        if(left != -1 and self.__heap_arr[left] > self.__heap_arr[index]):
            max=left
        else:
            max=index

        if (right != -1 and right < self.__count and  self.__heap_arr[right] > self.__heap_arr[max]):
            max = right
        #swap the numbers
        if max != -1 and max != index:
            print("swapping %d"%(self.__heap_arr[index]) + "and %d " %(self.__heap_arr[max]))

            temp=self.__heap_arr[index]
            self.__heap_arr[index]=self.__heap_arr[max]
            self.__heap_arr[index]=temp
            self.percolateDown(max)

    def buildHeap(self):
        index = self.__count-1
        while index > -1 :
            print("index=%d "%(index))
            self.percolateDown(index)
            index-=1
        # One by one extract elements
        for i in range(self.__count-1, 0, -1):
            self.__heap_arr[i], self.__heap_arr[0] = self.__heap_arr[0], self.__heap_arr[i]   # swap
            self.percolateDown(i)


a=[9,5,2,7,8,3,11,5,4,6]
heap = binary_heap(a)
heap.printHeap()
heap.buildHeap()
heap.printHeap()


