"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def __init__(self):
        self.actual_number=1034673429707
    def guess(self,number):
        if number == self.actual_number:
            return 0
        elif number > self.actual_number:
            return -1
        else:
            return 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <1:
            return 0
        low=1
        high=n
        iterations=0
        mid=0
        while low <= high:
            iterations+=1
            mid=low+(high-low)//2
            result=self.guess(mid)
            print("iterations=%d,low=%d,high=%d" % (iterations, low, high))
            if result == 0:
                break
            elif result == 1:
                low=mid+1
            elif result == -1:
                high=mid-1
        return mid

sol=Solution()
print(sol.guessNumber(100000000000000))
