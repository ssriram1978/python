"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""
"""
Sort the list based upon start time.
Start a loop while you haven't reached the end of the list:
    Check if the next (start,end) overlaps with current (start,end)
    If so, then, 
        merge them into one 
        delete both the items from the list and 
        replace the new one at this location in the list.
        Make this new item as the current item.
    Else:
        move the current item as the next item.
"""

"""
1. Sort the intervals based on increasing order of 
    starting time.
2. Push the first interval on to a stack.
3. For each interval do the following
   a. If the current interval does not overlap with the stack 
       top, push it.
   b. If the current interval overlaps with stack top and ending
       time of current interval is more than that of stack top, 
       update stack top with the ending  time of current interval.
4. At the end stack contains the merged intervals.
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return
        #declare a list that can hold all the elements
        list_elements=[]
        #sort the list based upon the start index
        start_index_based_sorted_list=sorted(intervals,key=lambda x:x[0])
        #now that you have sorted the list, all I need to check is adjacent elements
        #push the first item from the interval into the stack
        list_elements.append(intervals[0])
        for index in range(1,len(intervals),+1):
            current_element=start_index_based_sorted_list[index]
            print("current element="+str(current_element))
            top_element_in_heap=list_elements[len(list_elements)-1]
            if top_element_in_heap[0] <= current_element[0] and top_element_in_heap[1] >= current_element[0]:
                # check if the start of top element in heap is less than the start of the current element
                # check if the end of the top element in heap is greater than the start of the current element
                # if both the conditions are true, then, there is an overlap.
                # set the end of the top element in the heap to the end of the current element
                if top_element_in_heap[1] <=current_element[1]:
                    top_element_in_heap[1]=current_element[1]

            elif top_element_in_heap[0] >=current_element[0] and top_element_in_heap[0] < current_element[1]:
                    top_element_in_heap[0]=current_element[0]
                    # check if the start of top element in heap is greater than the start of the current element
                    # check if the start of the top element in heap is lesser than the end of the current element
                    # if both the conditions are true, then, there is an overlap.
                    # set the start of the top element in the heap to the start of the current element
                    if current_element[1] >=top_element_in_heap[1]:
                        top_element_in_heap[1]=current_element[1]
            else:
                #no overlap, just add it to the heap
                list_elements.append(current_element)
        return list_elements
sol=Solution()
list=[[1,3],[8,10],[15,18],[2,6]]
list_elements=sol.merge(list)
print(list_elements)
