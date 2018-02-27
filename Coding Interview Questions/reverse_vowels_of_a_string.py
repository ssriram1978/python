"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
"""
start from the middle of the string.
if there are even number of elements, then there are two mid elements.
if there are odd number of elements, then there is one mid element.
In both the above said cases, find the vowels one on the left of the mid and other on the right of the mid and swap them.
Keep doing this until you reach the end of the string.
"""
from collections import defaultdict

class Solution:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or type(s) != str or len(s)==0:
            return None

        list_of_chars=[x for x in s]
        length_of_string = len(list_of_chars)
        left = 0
        right = 0

        if length_of_string%2 == 0:
            #even
            left=length_of_string//2-1
            right=length_of_string//2
        else:
            #odd
            left=length_of_string//2
            right=length_of_string//2+1

        #print("left=%d" % (left) + "Right=%d" % (right))

        vowels_dict=defaultdict(int)
        vowels_dict['a']=1
        vowels_dict['e']=1
        vowels_dict['i']=1
        vowels_dict['o']=1
        vowels_dict['u']=1

        while left >=0 and right <= length_of_string-1:
            while left >=0 and vowels_dict[list_of_chars[left]] != 1:
                left-=1
            while right <= length_of_string-1 and vowels_dict[list_of_chars[right]] != 1:
                right+=1

            #print("Found vowels at left=%d"%(left)+"Right=%d"%(right))

            if left < 0 or right == length_of_string:
                break
            temp=list_of_chars[left]
            list_of_chars[left]=list_of_chars[right]
            list_of_chars[right]=temp
            left-=1
            right+=1
        #print(list_of_chars)
        output = ''.join(list_of_chars)
        return output

sol=Solution()
print(sol.reverseVowels("sriram"))

