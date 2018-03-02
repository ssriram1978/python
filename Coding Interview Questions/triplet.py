
"""
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet and return true. Else return false.
For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
then there is a triplet (12, 3 and 9) present in array whose sum is 24.
"""
"""
Algorithm-1:
------------
Sort the input array. o(n*logn) - Merge sort.
Run a outer loop that iterates over all the elements.
Run an inner loop that ierates over all the elements.
Get the pair of elements i and j
Perform a Binary search on the sorted list to see if target-(i+j) is there O(log n)
If found, then return the value.

O(n^2) + O(nlogn).

Algorithm-2
------------
Define an output list=[]

Define an output hash table that contains the triplets as the key.
Example if the possible match is (0,2,4), then there will be 6 such key value pairs:
key=(0,2,4)
key=(0,4,2)
key=(2,0,4)
key=(2,4,0)
key=(4,0,2)
key=(4,2,0)
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
from collections import defaultdict

class Solution:

    def generate_index_list(self,list_of_indexes):
        #base case
        if len(list_of_indexes) == 0:
            return []
        if len(list_of_indexes) == 1:
            return list_of_indexes

        output_list=[]

        for index in range(len(list_of_indexes)):
            #Permute the remaining elements

            items_before=list_of_indexes[:index]
            items_after=list_of_indexes[index+1:len(list_of_indexes)]
            items_before_after=[]
            items_before_after.extend(items_before)
            items_before_after.extend(items_after)

            rest_of_the_list=self.generate_index_list(items_before_after)

            for content in rest_of_the_list:
                permutation = []
                permutation.append(list_of_indexes[index])
                if type(content) is list:
                    permutation.extend(content)
                elif type(content) is int:
                    permutation.append(content)

                output_list.append(permutation)

        return output_list


    def check_for_duplicates(self,list_of_indexes,output_hash_table):
        isDuplicate=False
        index_list_array=self.generate_index_list(list_of_indexes)
        #print(index_list_array)

        for index_list in index_list_array:
            if output_hash_table[tuple(index_list)] == 1:
                isDuplicate=True
                break

        return isDuplicate

    def find3Numbers(self,array,sum):
        if array==None or array==[]:
            return None
        #sort the input array o(n*log(n))
        sorted_array=sorted(array)
        #define an output array that captures tri elements.
        output_array=[]

        #define a hash table indexed by one of the tri element and that returns a list of all possible tri elements.
        output_hash_table=defaultdict(int)

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
                    #make sure that these 3 elements are not there in the output hash table.
                    list_of_indexes = [current_index, left, right]
                    if self.check_for_duplicates(list_of_indexes,output_hash_table) == False:
                        output_array.append((sorted_array[current_index],sorted_array[left],sorted_array[right]))
                        output_hash_table[tuple(list_of_indexes)]=1
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

