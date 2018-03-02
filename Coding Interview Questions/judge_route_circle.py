"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""
"""
U (up) moves x co-ordinate by +1 and and D (Down) moves x co-ordinate by -1.
L (Left) moves y co-ordinate by +1 and R (Right) moves y co-ordinate by -1.
Read the string from left to right and increment  x and y co-ordinates accordingly.
Return True if x and y co-ordinates are 0 else return false.
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
