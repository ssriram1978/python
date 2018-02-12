"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
"""
1) Create an empty Trie.
2) Do following for every word:-
    a) Insert reverse of current word.
    b) Also store up to which index it is 
       a palindrome.
3) Traverse list of words again and do following 
   for every word.
    a) If it is available in Trie then return true
    b) If it is partially available
         Check the remaining word is palindrome or not 
         If yes then return true that means a pair
         forms a palindrome.
         Note: Position upto which the word is palindrome
               is stored because of these type of cases.
"""

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """