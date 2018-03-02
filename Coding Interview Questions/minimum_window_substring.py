"""
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
"""
"""
For every character in S, add it to a dictionary with the key as the character and the index as the value. O(n)
For every character in T: O(m)
    Look up the character in the dictionary and get the list. O(1)
    Keep appending this list to an output_list.
Now, you have the output list which contains the list of each character index.
You need to find the minimal distance between the indexes.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
