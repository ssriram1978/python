"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
"""
Algorithm:
----------
If the string is empty, return True

Find the length of the string.

If the string is of length 1, return True

If the length is even, then,
    left index is set to the left mid character
    right index is set to the right mid character
If odd,
    left index is set to the left of the mid character
    right index is set to the right of the mid character

While left index is >=0 and right index <=length(string)-1:
    if string[left_index] == string[right_index]    
        move left index towards the beginning of the string (decrement the index by 1)
        move right index towards the end of the string (increment the index by 1).

If left index is not equal to 0 or right index is not equal to len(string)-1, then,
    return False
Else
    return True 
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or len(s) == 1:
            return True

        #strip off white space
        list=s.strip()
        input_string=""
        for character in s:
            ascii_char_val=ord(character)
            if ascii_char_val >= ord('a') and ascii_char_val <= ord('z'):
                input_string+=character
            elif ascii_char_val >= ord('A') and ascii_char_val <= ord('Z'):
                input_string += chr(ord('a') + (ascii_char_val-ord('A')))
        #print(input_string)

        length_of_string=len(input_string)
        left_index=0
        right_index=0
        mid = length_of_string // 2
        if length_of_string%2==0:
            #even
            left_index=mid-1
            right_index=mid
        else:
            #odd
            left_index=mid-1
            right_index=mid+1

        while left_index >=0 and right_index <=length_of_string-1:
            if input_string[left_index]==input_string[right_index]:
                left_index-=1
                right_index+=1
            else:
                break

        if left_index !=-1 or right_index != length_of_string:
            return False
        else:
            return True

sol=Solution()
string="abcdcba"
print("sol.isPalindrome(%s) returned %s"%(string,sol.isPalindrome(string)))
string="abcddcba"
print("sol.isPalindrome(%s) returned %s"%(string,sol.isPalindrome(string)))
string="abcddcbad"
print("sol.isPalindrome(%s) returned %s"%(string,sol.isPalindrome(string)))
string="aabcddcba"
print("sol.isPalindrome(%s) returned %s"%(string,sol.isPalindrome(string)))
string="A man, a plan, a canal: Panama"
print("sol.isPalindrome(%s) returned %s"%(string,sol.isPalindrome(string)))
