"""
ou are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
class Solution:

    def climbStairs_Memoization(self, n, cache):
        if n == 1 or n == 2:
            return 1
        else:
            if not cache[n-1]:
                cache[n-1] = self.climbStairs_Memoization(n-1, cache)
            if not cache[n-2]:
                cache[n-2] = self.climbStairs_Memoization(n-2, cache)
            return cache[n-1] + cache[n-2]

    def climbStairs2(self, n):
        cache = [0] * n
        return self.climbStairs_Memoization(n, cache)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

sol = Solution()
print(sol.climbStairs2(400))