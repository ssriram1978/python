"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
"""
start from the mid of the string and check if the elements are palindrome and find the breaking point.
If you found a breaking point, then, try to check if characters need to be added to the left or right part of the 
string to make it a palindrome. If so, then, return those characters.
If you did not find any breaking point and the index is right at the middle, then, you need to return the whole reversed 
string to make it a palindrome.
"""

class Solution(object):

    def checkIsPalindrome(self,s):
        isPalindrome=False
        if s == None or len(s) == 0 or len(s) == 1:
            return isPalindrome

        mid = len(s)//2
        left = 0
        right = 0

        if len(s) % 2 == 0:
            # it is even
            # check the two mid characters to be equal
            mid1 = len(s) // 2
            mid2 = mid - 1
            if s[mid1] != s[mid2]:
                return isPalindrome
            left=mid1-1
            right=mid2+1
        else:
            # it is odd
            mid = len(s) // 2
            left = mid - 1
            right = mid + 1

        while left >=0 and right <=len(s)-1:
            if s[left]!=s[right]:
                break
            left-=1
            right+=1

        if left == -1 and right==len(s):
            isPalindrome=True

        return isPalindrome

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        isPalindrome = True
        output_string=""

        if s == None or len(s) == 0:
            isPalindrome=False
            return None

        if len(s) ==1:
            return s+s

        mid = len(s) // 2
        left = 0
        right = 0

        if len(s) % 2 == 0:
            # it is even
            # check the two mid characters to be equal
            mid1 = len(s) // 2
            mid2 = mid - 1
            if s[mid1] != s[mid2]:
                isPalindrome=False
            left = mid1 - 1
            right = mid2 + 1
        else:
            # it is odd
            mid = len(s) // 2
            left = mid - 1
            right = mid + 1

        if isPalindrome == False:
            output_string+=s[::-1]+s[1::]
            return output_string

        while left >= 0 and right <= len(s) - 1:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1

        if left == -1 and right == len(s):
            #perfect palindrome
            output_string=s
        elif left == -1 and right < len(s):
            #you still have some characters left on the left side of mid
            #but your right index reached the beginning
            #append the rest of the characters to the output string and return it as the palindrome
            output_string+=s[-1:right]+s
        elif left != -1 and right == len(s):
            #you still have some characters left on the right side of mid
            #but your left index reached the end
            #prepend the whole reversed string to the output string and return it as the palindrome
            output_string+=s[::-1]+s[1::]

        return output_string

sol=Solution()
print(sol.shortestPalindrome("abaa"))
