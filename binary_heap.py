class Heap:
    def __init__(self,list=None):
        self.__size=len(list)
        self.__arr=[0]
        self.__arr.extend(list)

        #build heap operation over list
        i=(self.__size//2)
        while(i >0):
            self.percolateDown(i)
            i-=1

    def percolateDown(self,position):
        lChild=2*position
        rChild=2*position+1
        small=-1

        if lChild <=self.__size:
            small=lChild
        if rChild <=self.__size and self.__arr[rChild]-self.__arr[lChild] < 0:
            small=rChild
        if small != -1:
            if self.__arr[small]-self.__arr[position] < 0:
                temp=self.__arr[position]
                self.__arr[position]=self.__arr[small]
                self.__arr[small]=temp
                self.percolateDown(small)

    def printHeap(self):
        i=1
        while i < self.__size:
            print(self.__arr[i])
            print(" ")
            i+=1


a=[9,5,2,7,8,3,11,5,4,6]
hp=Heap(a)
hp.printHeap()

