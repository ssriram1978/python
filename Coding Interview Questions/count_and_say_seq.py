"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
"""
Algorithm:
----------
Given nth sequence, you need to compute all the sequence from 0 to n-1 and then
compute nth sequence.
For this:
declare output_list=[] to capture all the sequences.
if n==1 return "1"
if n==2 return "11"
else
    Append "1","11" to output_list.
    Declare previous_element="11"
    Now, start a while loop until the count reaches n-1
        Declare next_element=""
        Read the current character from the previous element:
        count=1
        Start a while loop to count the consecutive occurrence of this character.
        Prepend this count in the next_element.
        Append the character to the next_element.

    Append next element to the output_list
    return output_list[n-1]
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
