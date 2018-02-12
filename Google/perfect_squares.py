"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

"""
A number can always be represented as a sum of squares of other numbers. 
Note that 1 is a square and we can always break a number as (1*1 + 1*1 + 1*1 + …). 
Given a number n, find the minimum number of squares that sum to X.

Examples:

Input:  n = 100
Output: 1
100 can be written as 102. Note that 100 can also be 
written as 52 + 52 + 52 + 52, but this
representation requires 4 squares.

Input:  n = 6
Output: 3

The idea is simple, we start from 1 and go till a number whose square is smaller than or equals to n. 
For every number x, we recur for n-x. Below is the recursive formula.

If n <= 3, then return n 
Else
   minSquares(n) = min {1 + minSquares(n - x*x)} 
                       where x >= 1 and x*x <= n 
Below is a simple recursive solution based on above recursive formula.
"""
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """


# A naive recursive Python program to
# find minimum number of squares whose
# sum is equal to a given number

# Returns count of minimum squares
# that sum to n
    if n <= 3:
        return n

    # getMinSquares rest of the table
    # using recursive formula
    res = n  # Maximum squares required
    # is n (1*1 + 1*1 + ..)

    # Go through all smaller numbers
    # to recursively find minimum
    for x in range(1, n + 1):
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1 + getMinSquares(n- temp))

    return res


# Driver program
print(getMinSquares(6))
