"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
3,3*3,3*3*3,3*3*3*3,3*3*3*3,3*3*3*3*3

"""
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #check if the number is fully divisible by 3
        #get the quotient
        #use this quotient and check if is fully divisible by 3
        #now take the quotient and the original number
        #multiply them and check if the result is fully divisible by 3
        if n==3:
            return True

        isDivisible=False
        if n%3 == 0:
            quotient=n/3
            if quotient%3==0:
                if (quotient*n)%3==0:
                    isDivisible=True

        return isDivisible

sol=Solution()
print(sol.isPowerOfThree(9))
print(sol.isPowerOfThree(21))
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(9**20))
print(sol.isPowerOfThree(9**21))

