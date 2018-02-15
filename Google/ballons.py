"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
"""
1. Prepare a sliding window that contains 3 elements.
2. For each of those sliding window, compute the product of those elements and store it in a output variable.
3. Prepare a list without the middle element of the sliding window and the rest of the original list.
4. Repeat step 1 to 3 recursively and keep computing the product and keep adding it to the output variable.

"""

class Solution:

    def prepare_sliding_window(self,nums,current_index):
        # prepare a window of 3 elements
        first = 0
        second = nums[current_index]
        third = 0
        product_of_three=0

        #if you are at the beginning of the list
        if current_index == 0:
            #your previous element is assumed to be 1
            first = 1
            #if your list just has one element
            if current_index == len(nums) - 1:
                #your end is also assumed to be 1
                third =1
            else:
                #your end is current index +1
                third = nums[current_index + 1]
        elif current_index == len(nums) - 1:
            #you are at the end
            #end is assumed to be 1
            third =1
            #your first is current index -1
            first = nums[current_index - 1]
        else:
            first=nums[current_index-1]
            third=nums[current_index+1]

        product_of_three=first*second*third
        print(first,second,third)
        return product_of_three

    def maxCoinsNonRecurse(self, nums, current_index):
        # base case
        sliding_window_product = 0
        final_sliding_window=0

        while nums != None or nums != [] or len(nums) != 0:
            # pick a sliding window from these two options left of the current index or right of the current index
            # the one that returns max is the window that you need to pick.
            # find the product of three numbers in the sliding window
            sliding_window_product = self.prepare_sliding_window(nums, current_index)
            sliding_window_product_left=0
            sliding_window_product_right=0
            index_to_be_deleted=0
            if current_index!=0:
                sliding_window_product_left = self.prepare_sliding_window(nums, current_index-1)
            if current_index!=len(nums)-1:
                sliding_window_product_right=self.prepare_sliding_window(nums, current_index+1)

            if sliding_window_product_left == 0:
                final_sliding_window+=max(sliding_window_product_right,sliding_window_product)
                if sliding_window_product > sliding_window_product_right:
                    index_to_be_deleted=current_index
                else:
                    index_to_be_deleted=current_index+1

            elif sliding_window_product_right==0:
                final_sliding_window+= max(sliding_window_product_left, sliding_window_product)
                if sliding_window_product > sliding_window_product_left:
                    index_to_be_deleted=current_index
                else:
                    index_to_be_deleted=current_index-1
            else:
                final_sliding_window=max(sliding_window_product_right,sliding_window_product_left)
                final_sliding_window+=max(sliding_window_product,final_sliding_window)
                if sliding_window_product > sliding_window_product_left and sliding_window_product > sliding_window_product_right:
                    index_to_be_deleted=current_index
                elif sliding_window_product_left > sliding_window_product and sliding_window_product_left > sliding_window_product_right:
                    index_to_be_deleted=current_index-1
                elif sliding_window_product_right > sliding_window_product and sliding_window_product_right > sliding_window_product_left:
                    index_to_be_deleted = current_index - 1

            # remove the current item from the list
            print("current_index to be removed=%d"%(current_index))
            nums.pop(index_to_be_deleted)

        return sliding_window_product

    def maxCoinsRecurse(self,nums,current_index):
        #base case
        sliding_window_product=0

        if nums==None or nums==[] or len(nums)==0:
            return sliding_window_product

        #find the product of three numbers in the sliding window
        sliding_window_product=self.prepare_sliding_window(nums,current_index)

        #remove the current item from the list
        #print("current_index to be removed=%d"%(current_index))
        nums.pop(current_index)

        #recurse to find the sum of all the sliding windows
        for index in range(len(nums)):
            sliding_window_product+=self.maxCoinsRecurse(nums,index)

        return sliding_window_product

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_result=0
        nums_temp=[]
        result = 0

        for index in range(len(nums)):
            #keep copying the original list into temp list.
            for num in nums:
                nums_temp.append(num)
            result=self.maxCoinsNonRecurse(nums_temp,index)
            #if result is greater than max, then, store this as the max result.
            print("result=%d"%(result))
            if result > max_result:
                max_result=result

            """
            for num in nums:
                nums_temp.append(num)
            result= self.maxCoinsNonRecurse(nums_temp, index)
            # if result is greater than max, then, store this as the max result.
            print("result=%d" % (result))
            if result > max_result:
                max_result = result
            """
        return max_result

sol=Solution()
print(sol.maxCoins([3, 1, 5, 8]))