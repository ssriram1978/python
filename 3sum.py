class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #declare the output return list
        return_list = []
        #declare three indexes for the 3 numbers to be found.
        index_1=0
        index_2=0
        index_3=0
        #start a while loop for the first index to be searched
        for index_1 in range(len(nums)) :
            #start a while loop for the second index to be searched
            for index_2 in range(len(nums)):
                #make sure not to reuse the same first index for the second index as well.
                if index_2 == index_1:
                    continue
                #start a while loop for the third index to be searched
                for index_3 in range(len(nums)):
                    #make sure not to reuse the first and second indexes for the third index.
                    if index_3 == index_1 or index_3 == index_2:
                        continue
                    #print("Index1=%d,index2=%d,index3=%d\n" %(index_1,index_2,index_3))
                    #Once you found the three variables that add up to 0 make sure not to add a duplicate entry into return_list.
                    if nums[index_1] + nums[index_2] + nums[index_3] == 0:
                        #print("Newly found values(%d,%d,%d) are at location(%d,%d,%d)\n" \
                       #%(array[index_1],array[index_2],array[index_3],index_1,index_2,index_3))
                        #start iterating the lists contained in return list
                        match_found = False
                        for list in return_list:
                            #declare a boolean match_found to be true
                            item_match=True
                            #for each value in the list if it does not match with the newly found values, then match_found=False
                            for value in list:
                                # break from the for loop if you did not find a match
                                if value != nums[index_1] and \
                                   value != nums[index_2] and \
                                   value != nums[index_3] :
                                    #print("Skipping this list because no match found...\n")
                                    item_match = False
                                    break
                            #do not add this list if item_match is true.
                            if item_match == True:
                                #print("Skipping this duplicate list.\n")
                                match_found=True
                                break;
                        if match_found == False:
                            new_list=[]
                            new_list.append(nums[index_1])
                            new_list.append(nums[index_2])
                            new_list.append(nums[index_3])
                            return_list.append(new_list)
                            #print("Append new_list to original return list.\n")
        #print(return_list)
        return return_list

sol = Solution()
#array=[-1, 0, 1, 2, -1, -4]
array=[0,3,0,1,1,-1,-5,-5,3,-3,-3,0]
print(sol.threeSum(array))
