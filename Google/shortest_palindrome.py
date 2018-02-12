"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
"""
start from the mid of the string and check if the elements are palindrome and find the breaking point.
If you found a breaking point, then, try to check if characters need to be added to the left or right part of the 
string to make it a palindrome. If so, then, return those characters.
If you did not find any breaking point and the index is right at the middle, then, you need to return the whole reversed 
string to make it a palindrome.
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
