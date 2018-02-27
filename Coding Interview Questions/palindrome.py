"""
To check if an integer is a palindrome:
In a loop until you have extracted all the digits from the end of the number,
    Extract each last digit of the integer via % 10 and keep adding it to result * 10.
If the computed reversed number is equal to the original number, then return True else return False.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0 or (x > 0 and x < 10):
            return False

        reversed_number = 0
        temp = x
        while temp != 0:
            reminder= temp%10
            reversed_number=reversed_number*10+ reminder
            #get rid of the last digit
            temp = temp//10

        if reversed_number == x:
            return True
        else:
            return False

sol=Solution()
print(sol.isPalindrome(112211))
