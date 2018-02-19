
"""
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet and return true. Else return false.
For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
then there is a triplet (12, 3 and 9) present in array whose sum is 24.
"""
"""
Algorithm:
----------
Sort the input array. o(n*logn) - Merge sort.
Define an output list=[]

Define an output hash table that contains the triplets indexed by each element as the key.
Example if the possible match is (0,2,4), then there will be 3 such key value pairs:
key=0 value=(0,2,4)
key=2 value=(0,2,4)
key=4 value=(0,2,4)
This is done to eliminate duplicate triplets like (0,2,4) (2,0,4) and (4,2,0) and use hashtable for o(1) lookups.
 
Start a loop that iterates over all the elements o(n)
    set left=0
    set right=length of array-1
    
    while left < right: o(n)
        check if array[current_index]+ array[left]+ array[right] == sum:
            If true, append it to the output list.
        else check if array array[current_index]+ array[left]+ array[right] < sum:
            Increment the left index by 1
        else
            Decrement the right index by 1
        
        If current index is equal to left, increment left by 1.
        If current index is equal to right, decrement right by 1.
            
return the output_list

This algorithm runs at order of n**2.
"""
class Solution:
    def find3Numbers(self,array,sum):
        if array==None or array==[]:
            return None
        #sort the input array o(n*log(n))
        sorted_array=sorted(array)
        output_array=[]
        for current_index in range(len(sorted_array)):
            left=0
            right=len(sorted_array)-1

            while left < right:
                #make sure that the 3 elements are unique.
                if left == current_index:
                    left+=1
                if right == current_index:
                    right-=1
                #compute the sum of all 3 elements.
                computed_sum=sorted_array[current_index]+sorted_array[left]+sorted_array[right]
                if computed_sum == sum:
                    #match found.
                    output_array.append((sorted_array[current_index],sorted_array[left],sorted_array[right]))
                    left+=1
                    right-=1
                elif computed_sum < sum:
                    #move left by one position
                    left+=1
                else:
                    #move right by one position
                    right-=1
                # make sure that the 3 elements are unique.
                if left == current_index:
                    left += 1
                if right == current_index:
                    right -= 1
        return output_array

sol=Solution()
# Driver program to test above function
A = [9,8,7,6,5,4,3,2,1,0]
print(sol.find3Numbers(A,6))
