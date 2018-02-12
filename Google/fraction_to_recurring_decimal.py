"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
"""
option a: get the reminder and multiply it by 10 and divide it to get the quotient and keep appending 
it to the string until 2 or 3 decimal place.
option b: get the floating result in a float variable and convert it to string and append ( and ) to the decimal part.
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
