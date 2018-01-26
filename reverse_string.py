#Write a function that takes a string as input and returns the string reversed.
#Example:
#Given s = "hello", return "olleh".

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=""
        #list=[]
        #for character in s:
        #    list.insert(0,character)
        #output=''.join(list)
        output=s[::-1]
        return output

sol=Solution()
print(sol.reverseString("Sriram"))