"""
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
"""
The basic idea is to find out the smallest result letter by letter (one letter at a time). Here is the thinking process for input "cbacdcbc":
find out the last appeared position for each letter; c - 7 b - 6 a - 2 d - 4
find out the smallest index from the map in step 1 (a - 2);
the first letter in the final result must be the smallest letter from index 0 to index 2;
repeat step 2 to 3 to find out remaining letters.
the smallest letter from index 0 to index 2: a
the smallest letter from index 3 to index 4: c
the smallest letter from index 4 to index 4: d
the smallest letter from index 5 to index 6: b
so the result is "acdb"
"""

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
