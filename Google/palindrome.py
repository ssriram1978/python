class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0 or (x > 0 and x < 10):
            return False

        sum = 0
        temp = int(x)
        while int(temp) != 0:
            sum = int(sum) * 10 + (int(temp)%10)
            print("temp=%d x=%d and sum=%d\n" % (temp, x,sum))
            temp = int(temp) / 10

        if int(sum) == int(x):
            return True
        else:
            return False

sol=Solution()
print(sol.isPalindrome(121))