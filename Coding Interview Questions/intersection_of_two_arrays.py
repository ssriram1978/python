"""
Find the intersection of two arrays.
array1=[1,3,5,7]
array2=[2,4,6,8,10]
Find the intersection of the two arrays.
"""
"""
Algorithm:
---------
Given two arrays, if the question is about finding the common elements betweeen the arrays,
1. Check if the arrays are sorted.
    If the arrays are sorted,
        Check if the start_array1 element is greater than or equal to start_array2 and
                     start_array1 element is less than end_array2:
                        If so: 
                            then there might be elements that overlap.
                        Else:
                            They are disjoint, return False.
                Else:
                    check if array2_start less than array1_end:
                        There might be an overlap.
                    Else:
                    They are disjoint, return False.
    Else:
        Sort the arrays array1 and array2 (O(nlogn) heap sort, quick sort, merge sort).
2. If len(array1) less than len(array2), 
        min=array1
   Else
        min=array2
3. For each element in min1, perform a binary search in min2 to check for a match. O(nlogn)
    If you found a match, append the element to an output list
    
    3a. As an optimization: Remember the location where you found a match for the element in array2,
            Perform a linear seach from that location O(n)

4. Return the output list. 

"""

class Solution:
    def binary_search(self,array,element):
        start=0
        end=len(array)-1
        found_match=False
        while start <= end:
            mid = start + (end - start) // 2
            if array[mid] == element:
                found_match=True
                break
            elif array[mid] > element:
                end = mid - 1
            else:
                start = mid + 1
        return found_match

    def find_intersection(self,array1,array2):
        array1=sorted(array1)
        array2=sorted(array2)

        if len(array1) <=  len(array2):
            minarray=array1
            maxarray=array2
        else:
            minarray=array2
            maxarray=array1

        output_list=[]
        for element in minarray:
            if self.binary_search(maxarray,element) == True:
                output_list.append(element)
        return output_list

sol=Solution()
array1=[2,4,6,8,10]
array2=[1,3,5,7,9,10]
print(sol.find_intersection(array1,array2))
