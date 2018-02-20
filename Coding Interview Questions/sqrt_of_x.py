"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we want to return an integer, the decimal part will be truncated.
"""
"""
Algorithm:
----------
A Better Solution to do Binary Search.

Let  's' be the answer.  We know that 0 <=  s <= x.

Consider any random number r. 

    If r*r <= x, s >= r

    If r*r > x, s < r. 
Algorithm:
1) Start with 'start' = 0, end = 'x',
2) Do following while 'start' is smaller than or equal to 'end'.
      a) Compute 'mid' as (start + end)/2
      b) compare mid*mid with x.
      c) If x is equal to mid*mid, return mid.
      d) If x is greater, do binary search between mid+1 and end. In this case, we also update ans (Note that we need floor).
      e) If x is smaller, do binary search between start and mid-1
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
