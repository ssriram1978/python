"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
"""
Declare hamming_distance variable as 0.
Start a while loop which goes while x is not equal to 0 and y is not equal to 0.
    And x with 1 to check if LSB is set. If so, set a variable x_1 as True else variable x_1=False
    And y with 1 to check if LSB is set. If so, set a variable y_1 as True else variable y_1=False
    If x_1 == True and y_1==False or x_1==False and y_1==True:
        hamming_distance+=1
    Right shift x and y by 1.
If x is not equal to 0:
    You still have some left overs on x:
    Start a while loop until x is not equal to 0:
        And x with 1 and check if LSB is set. If so, increment hamming_distance by 1 because 
        you already know that y is 0.
Else:
If y is not equal to 0:
    You still have some left overs on y:
    Start a while loop until y is not equal to 0:
        And y with 1 and check if LSB is set. If so, increment hamming_distance by 1 because 
        you already know that x is 0.
return hamming_distance.
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
