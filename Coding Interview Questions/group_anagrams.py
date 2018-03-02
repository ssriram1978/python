"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
"""
Start a loop that walks over each word in the list O(n) where n is the number of words in the list.
    Sort each word in the order of XlogX where X is the number of characters in each word.
    Add this sorted word into a dictionary with
        Key=sorted word
        Value=list of actual words.
Now walk through the dict to fetch the key,value pairs and append only the values to a output list and return it. 
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
