class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #define an empty hash table
        hash_table = {}
        #define an empty output list
        output = []
        #define a temp list
        list=[]
        #start a for loop for the size of the input list
        for index in range(len(nums)):
            #check if there is already a list in the hash table for that number
            try:
                list = hash_table[nums[index]]
            except:
                list=[]
            #add the index to the list and put it back in the hash table.
            list.append(index)
            hash_table[nums[index]]=list

        print(hash_table)

        #start a loop to iterate over the numbers in the input list
        for index in range(len(nums)):
            number=nums[index]
            #find the differece between the target and the current number
            result = target-number
            #print(result)
            #check if the result is found in the dictionary.
            try:
                list = hash_table[result]
                #if you found a list for that number, then make sure that you are not referring to the self number.
                if list != None:
                    item_found = False
                    #iterate the list and make sure to find the index
                    # that does not clash with the index of the current number that you are searching.
                    current_index=index
                    for item in list:
                        if item != current_index:
                            item_found=True
                            break
                    #add this current index and the item if you found a match
                    if item_found == True:
                        output.append(item)
                        output.append(current_index)
                        break
            #skip this number and continue to the next number.
            except:
                continue

        return output

sol=Solution()
array=[3,2,3]
print(sol.twoSum(array,6))