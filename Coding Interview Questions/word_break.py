"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.
"""

from collections import defaultdict

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        isMatch=False
        """
        1. Add all wordDict to a dictionary.
        2. Starting at index 0 search for a character or a bunch of characters in dictionary.
        3. Keep accumulating characters and perform a lookup until you find a match.
        4. Split the word right at the point you found a match.
        5. Perform a lookup of the remaining word in the dictionary.
        6. If you did not find the remaining word, then, repeat the steps 2 to 4 until you find a match.
        7. Repeat this until you reach the end of the input string.
        """
        #add words to the dictionary
        word_dict=defaultdict(int)
        for words in wordDict:
            word_dict[words]=1

        temp_word=""
        for index in range(0,len(s),+1):
            temp_word+=s[index]
            if word_dict[temp_word]==-1:
                continue
            elif word_dict[temp_word]==1:
                #match found
                if index == len(s)-1:
                    isMatch=True
                    break
                else:
                    #split the word and store it in the
                    temp_word=""
        return isMatch


sol=Solution()
dict=["leet","code","help","needed"]
print(sol.wordBreak("leetcode",dict))
print(sol.wordBreak("leetneededhelphel",dict))
