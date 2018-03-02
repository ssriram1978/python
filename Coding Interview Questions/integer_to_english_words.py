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

    Base case: If the start variable is length of the word - 2,
    then return lookup just the integer value of the number in the dictionary and return the output back to the recursive call.

    diff = length_of_word - start

    if length_of_word  == 2:
        #12 we are accessing 12
        return output= dict lookup (current digit+next digit)
    if diff == 3:
        #123 we are accessing 1
        output= dict lookup (current digit) + dict look up (10**diff)
        output+=recurse (number,start+1)
    elif diff == 4:
        #1234  we are accessing 1
        output=dict lookup (current digit) + dict look up (10**diff)
        output+=recurse (number,start+1)
    elif diff == 5:
        #12345  we need to access 12
        res=diff%3
        if res == 2
            if current digit.*********TODO****************
        output= dict lookup (current digit,next digit) + dict look up (10**(diff-mod))
        output+=recurse (number,start+res)
    elif diff == 6:
        #123456 we are accessing 1
        res=diff%3
        if res == 0
            output= dict lookup (current digit) + dict look up (10**(diff//3))
        else
            output= dict lookup (current digit,...res)
        output+=recurse (number,start+res)
    else if diff == 7:
        #1234567 we are accessing 1
        res=diff%3
         if res == 1
            output= dict lookup (current digit) + dict look up (10**(diff//3))
            
        return output=dict lookup (current digit) + dict look up (1000000)

    next_word = Fetch the word of next integer by invoking a recursive call incrementing the start variable by 1.
    current word = dict lookup (current digit) + dict lookup (10 * (length_of_word-start))

    return output=current word + next word.
"""
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
