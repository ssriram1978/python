"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
"""
In the first sweep, loop over the characters:
    if you do not find a character in a hash table, then add it to the hash table with the key as character and index as the value
    If you find the character in hash table, then, delete it.
Once you exit the loop, sort the hash table based upon the value and return the character at index 0.

"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
