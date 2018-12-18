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

If n is the total number of stairs and
m is the max number of steps to climb at one time.
ClimbStairs(n) = ClimbStairs(n-1) + ClimbStairs(n-2) + ClimbStairs(n-m)

"""


class Solution:

    def recurse_n_steps_memo(self, n, m, cache):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            if m == 1:
                return 1
            elif m >= 2:
                return 2
        else:
            for index in range(m):
                if n-index-1 < 0:
                    continue
                if not cache[n - index - 1]:
                    cache[n - index - 1] = self.recurse_n_steps_memo(n - index - 1,
                                                                     m,
                                                                     cache)
            total_ways = 0
            for index in range(m):
                if n-index-1 < 0:
                    continue
                total_ways += cache[n - index - 1]
            return total_ways

    def climbStairs_recursion_n_steps_memo(self, n, m):
        cache = [0] * n
        if n == 0:
            return 0
        return self.recurse_n_steps_memo(n, m, cache)

    def climbStairs_recursion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs_recursion(n - 1) + self.climbStairs_recursion(n - 2)

    def non_recurse(self, n, m):
        dp = [0] * (n+1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            if m == 1:
                return 1
            else:
                return 2
        else:
            dp[0] = 1
            dp[1] = 1
            for index in range(2,n+1):
                for index2 in range(1,m+1):
                    if index-index2>=0:
                        dp[index] += dp[index-index2]
            return dp[n]

sol = Solution()
total_stairs = 5

for index in range(total_stairs):
    print("Ways to climb {} stairs = {} two stairs at a time.".format(index,
                                                                      sol.climbStairs_recursion(index)))
ways = 3
for index in range(total_stairs):
    print("Ways to climb {} stairs max of {} stairs at a time  "
          "using memo = {}.".format(index,
                                    ways,
                                    sol.climbStairs_recursion_n_steps_memo(
                                        index,
                                        ways)))

ways = 3
for index in range(total_stairs):
    print("Non recursive: Ways to climb {} stairs max of {} stairs at a time  "
          "using memo = {}.".format(index,
                                    ways,
                                    sol.non_recurse(
                                        index,
                                        ways)))

ways = 4
for index in range(total_stairs):
    print("Ways to climb {} stairs max of {} stairs at a time  "
          "using memo = {}.".format(index,
                                    ways,
                                    sol.climbStairs_recursion_n_steps_memo(
                                        index,
                                        ways)))

ways = 4
for index in range(total_stairs):
    print("Non recursive: Ways to climb {} stairs max of {} stairs at a time  "
          "using memo = {}.".format(index,
                                    ways,
                                    sol.non_recurse(
                                        index,
                                        ways)))

"""
4 stairs 2 at a time:
1111
112
121
22
211

3 stairs 3 at a time:
111
12
21
3

4 stairs 3 at a time:
1111
121
211
112
13
31
22
"""
