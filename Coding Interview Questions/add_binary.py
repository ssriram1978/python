"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
"""
Declare output string as "".
In a loop start reading the characters from "a" and "b" from the end of the string.
If the characters are 1 and 1, then write 0 to an output string and keep the carry as 1.
If the characters are 1 and 0, or 0 and 1, . 
    If there is a carry, then, prepend 0 to the output string and keep carry as 1. 
    Else
    Prepend 1 to the output string
    
If the characters are 0 and 0, 
    If there is a carry, then, prepend 1 to the output string.
    Else
    Prepend 0 to the output string.
Return output string.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
