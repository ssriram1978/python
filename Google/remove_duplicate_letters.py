#Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once.
#You must make sure your result is the smallest in lexicographical order among all possible results.
#Example:
#Given "bcabc"
#Return "abc"
#Given "cbacdcbc"
#Return "acdb"
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_string=set(s)
        set_string=sorted(set_string)
        return set_string

sol=Solution()
print(sol.removeDuplicateLetters("cbacdcbc"))