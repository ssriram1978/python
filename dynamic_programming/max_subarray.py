"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

nums = [-2,1,-3,4,-1,2,1,-5,4],
dp = [,,,,,,,,,,,,,,,]
dp[i] = max(nums[i]+dp[n-2], dp[n-1])

"""

"""
Alg:
---
nums = [-2,1,-3,4,-1,2,1,-5,4],
dp = [,,,,,,,,,,,,,,,]
dp[i] = max(nums[i]+dp[n-2], dp[n-1])
"""

def max_subarray(nums):
    subarray=[]
    if len(nums) is 0:
        return subarray
    dp = [0] * len(nums)
    max_dp_index = 0
    max_dp_value = 0
    for index in range(len(nums)):
        if index == 0:
            dp[index] = nums[index]
            max_dp_value = nums[index]
            max_dp_index = index
        else:
            dp[index] = max(nums[index], nums[index]+dp[index-1])
        if dp[index] > max_dp_value:
            max_dp_value = dp[index]
            max_dp_index = index
    for index in range(max_dp_index,-1,-1):
        subarray.insert(0, nums[index])
        max_dp_value -= nums[index]
        if max_dp_value <=0:
            break
    return subarray

input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(input))
input = [-2, -1]
print(max_subarray(input))