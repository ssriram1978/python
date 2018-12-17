
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
n = Total number of homes.
P[] = value of each home.
Max Revenue at nth home is
a. If nth home is robbed.
(nth home is included and max possible revenue at n-2 is computed.)
b. If nth home is not robbed.
(max revenue at n-1 is just returned)
R(n) = max (P[n] + R(n-2), R(n-1))
Base case: R(0) = 0, R(1) = 1
"""

def find_max_profit2(current_index, profit_array, revenue_cache):
    max_profit = 0
    if current_index == 0:
        max_profit = 1
    elif current_index == 1:
        max_profit = max(profit_array[0], profit_array[1])
    else:
        revenue_n_1 = 0
        if not revenue_cache[current_index-1]:
            revenue_n_1 = find_max_profit2(current_index-1,
                                           profit_array,
                                           revenue_cache)
        revenue_n_2 = 0
        if not revenue_cache[current_index-2]:
            revenue_n_2 = find_max_profit2(current_index-2,
                                           profit_array,
                                           revenue_cache)
        max_profit = max(profit_array[current_index] + revenue_n_2,
                          revenue_n_1)
    return max_profit

def find_max_profit(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        elif i == 1:
            dp[i] = max(nums[0], nums[1])
        else:
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

nums = [2,7,1,3,9]
print(find_max_profit(nums))
cache = [0] * len(nums)
print(find_max_profit2(len(nums)-1, nums, cache))
