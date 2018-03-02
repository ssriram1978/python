"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
"""
Prepare a dict of digit as key and words as the value.
From 1 to 20 and then 30,40,50,....100,1000,10000,100000,1000000,10000000,100000000,1000000000
Convert the number to a string and invoke a function that does computes the string equivalent of the 
number and returns it back to the caller with start variable set to 1.
    
    Declare an output_string variable to be ""
    
    Base case: If the start variable is length of the word -1, then return lookup just the interger
    value of the number in the dictionary and return the output back to the recursive call.
    
    next_word = Fetch the word of next integer by invoking a recursive call incrementing the start variable by 1.
    
    if length_of_word - start == 5:
        return output= dict lookup (current digit) + dict lookup (10) /******TODO******/
    else if length_of_word - start == 6:
       return output= dict lookup (current digit) * (10)
    current word = dict lookup (current digit) + dict lookup (10 * (length_of_word-start))
    
    return output=current word + next word.
    
The base case is if the start

"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
