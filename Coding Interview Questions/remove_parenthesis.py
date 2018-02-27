"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
"""
Algorithm:
----------
parenthesis_open='('
parenthesis_close=')'
Convert the input string into a list.
Declare an output list that captures all possible valid strings.
Declare an invalid character list which captures the index of all the characters which are invalid.
Declare a stack that is used to capture all the characters in the list.
For every character in the list, do the following:
    If the character is a letter, then, continue
    If the character is parenthesis_open, then, push it to a stack.
    If the character is parenthesis_close, then 
        pop the element from the stack and check if it is parenthesis_open
            if it is open, then continue with the next character in the string
            else:
                you found an invalid parenthesis.
                There are two possible options
                1. Assume this current parenthesis is invalid and store its index in the invalid character list.
                2. Assume this current parenthesis is valid and walk backwards towards the 
                   beginning of the string and locate the invalid parenthesis and store the index
                   in the invalid character list.
Iterate over the list of invalid character indexes and :
    Form individual strings without those indexes and append it to an output list
return the output list.
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
