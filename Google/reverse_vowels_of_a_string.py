"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
"""
start from the middle of the string.
if there are even number of elements, then there are two mid elements.
if there are odd number of elements, then there is one mid element.
In both the above said cases, find the vowels one on the left of the mid and other on the right of the mid and swap them.
Keep doing this until you reach the end of the string.
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
