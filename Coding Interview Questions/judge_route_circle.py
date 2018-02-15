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
The move ‘G’ changes either x or y according to following rules.
a) If current direction is North, then ‘G’ increments y and doesn’t change x.
b) If current direction is East, then ‘G’ increments x and doesn’t change y.
c) If current direction is South, then ‘G’ decrements y and doesn’t change x.
d) If current direction is West, then ‘G’ decrements x and doesn’t change y.

The moves ‘L’ and ‘R’, do not change x and y coordinates, they only change direction according to following rule.
a) If current direction is North, then ‘L’ changes direction to West and ‘R’ changes to East
b) If current direction is East, then ‘L’ changes direction to North and ‘R’ changes to South
c) If current direction is South, then ‘L’ changes direction to East and ‘R’ changes to West
d) If current direction is West, then ‘L’ changes direction to South and ‘R’ changes to North.
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """