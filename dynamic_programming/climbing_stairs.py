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
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if not cache[n - 1]:
                cache[n - 1] = self.recurse_n_steps_memo(n - 1,
                                                         m,
                                                         cache)
            if not cache[n - 2]:
                cache[n - 2] = self.recurse_n_steps_memo(n - 2,
                                                         m,
                                                         cache)
            total_ways = 0
            for index in range(1, m + 1):
                total_ways += cache[n - index]
            return total_ways

    def climbStairs_recursion_n_steps_memo(self, n, m):
        cache = [0] * n
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

    def slide_window_by_one(self, list_of_values):
        value_to_be_appended = list_of_values[-1] + list_of_values[-2]
        list_of_values.append(value_to_be_appended)
        del(list_of_values[0])

    def non_recurse(self, n, m):
        total_ways = 0
        if n == 0:
            total_ways = 0
        elif n == 1:
            total_ways = 1
        elif n == 2:
            total_ways = 2
        else:
            last_m_elements = [0] * m
            for index in range(0, n):
                if index == 0:
                    last_m_elements[index]=1
                elif index ==1:
                    last_m_elements[index]=1
                else:
                    self.slide_window_by_one(last_m_elements)
            for index in range(0, m):
                total_ways += last_m_elements[index]
        return total_ways


sol = Solution()
total_stairs = 5
for index in range(total_stairs):
    print("Ways to climb {} stairs = {}.".format(index,
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

"""
1111
112
121
22
211
"""
