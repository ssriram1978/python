"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
"""
The given string S may or may not be a palindrome.

Note that you cano convert it to a palindrome by adding characters only to the front of it.

Start from the mid of the string and check if the elements are palindrome and find the breaking point.

If the string is of odd length, then, there is only one mid character.
If the string is of even length, then, there are two mid characters:
    Example: abcddcba Here dd are mid characters.
    If the mid characters are not equal:
        Example: abcdecba 
        Return the palindrome as the whole string reverse appended to the beginning of S. abcdecbabcdecba
Else:
Define a left and right pointer on the either side of the middle character.
Keep checking the left and right pointer content to be equal.
Break if the left and right pointer are not pointing to character that do not match.
After breaking out from the loop,
    
    Check if your left pointer reached beyond the beginning of the word, 
    and your right pointer, still did not reach the end, 
    then, you need to append all those characters to the beginning of the string to make it a palindrome.
    Example: acdbdcabc In this case, left pointer will be at -1 and right will be at b.
    Now append b and c to the front of the word to make it a palindrome. (bcacdbdcabc)
    
    If your left pointer did not reach the beginning of the word, 
    then you can only append the whole word in reverse order to the beginning of the word to make it a palindrome
    Example: acdbdda Here left and right pointer will break at c and d. The only way to make it palindrome is 
    by copying the whole word in reverse to the beginning of the palindrome (acdbddacdbdda)
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
