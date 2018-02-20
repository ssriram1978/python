"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

"""
Algorithm:
----------
Declare an output temp variable to be -1 which will be used to store the index of the first match.
Search for the first occurance of the first character of needle in haystack.
If found, then, do the following:
    Store the index of the first character match as the output temp variable.
    Check if the characters preceding needle match the characters preceding haystack.
        If they match,store and return the output temp variable.
    Else
        Reset the output temp variable to -1
Return the output temp variable
    
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == None or needle == "" or haystack == None or haystack == "":
            return -1

        #declare first found index to be -1
        firstFoundIndex=-1

        for current_index in range(len(haystack)):
            #check if the first character in needle matches with the character in haystack at current_index.
            if needle[0] == haystack[current_index]:
                #declare a temp variable that stores this current index
                firstPossibleMatch=current_index
                #check if the rest of the characters preceding needle match
                # with the characters preceding haystack at current index.
                needle_index=1
                haystack_index=current_index+1
                while needle_index < len(needle):
                    if needle[needle_index] != haystack[haystack_index]:
                        #No match found,break from the while loop
                        break
                    needle_index+=1
                    haystack_index+=1

                if needle_index == len(needle):
                    #complete match found
                    firstFoundIndex=firstPossibleMatch
                    break

        return firstFoundIndex

sol=Solution()
index=sol.strStr("hello world","world")
print(index)
index=sol.strStr("wonworwwwowobwwwolwwwwol","wol")
print(index)
