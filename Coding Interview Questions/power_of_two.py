"""
Given an integer, write a function to determine if it is a power of two.
"""
"""
2=10
4=100
8=1000
16=10000
...
If it is a 64 bit number, keep extracting the LSB 64 times and make sure that you have just one 1 and 63 zeros.

"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isPowOfTwo=False
        mask=1
        found_one=False
        for index in range(0,64):
            if n&mask==1:
                if found_one==True:
                    isPowOfTwo=False
                    break
                else:
                    found_one=True
            #remember to left shift the number by 1
            n=n>>1

        if found_one==True and index==63:
            isPowOfTwo=True
        return isPowOfTwo

sol=Solution()
print(sol.isPowerOfTwo(1024))
print(sol.isPowerOfTwo(4096))
print(sol.isPowerOfTwo(100))
print(sol.isPowerOfTwo(1125899906842624))
