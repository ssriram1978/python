#Write a function that takes a string as input and returns the string reversed.
#Example:
#Given s = "hello", return "olleh".
"""
find the middle of the string
if there are even number of elements, then there are two mid elements, swap them.
if there are odd number of elements, then there is one mid element. swap elements on either side of the mid element.
continue the above said steps in a loop until you reach the end of the string.
"""

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