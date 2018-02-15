"""
Given an integer, write a function to determine if it is a power of two.
"""
"""
check if the number is fully divisible by 2
get the quotient
use this quotient and check if is fully divisible by 2
now take the quotient and the original number
multiply them and check if the result is fully divisible by 2
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
