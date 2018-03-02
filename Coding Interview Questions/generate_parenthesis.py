"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
"""
This involves recursion.
Pass a string variable to the recursive loop.
Base case is if the string variable is of size n*2 print it or add it to a list and return.
Else
    If start index is less than n:
        Append the opening parenthesis to the string.
        Pass it recursively to self with start index incremented by 1.
    Else:
        If end index is less than n:
        Append the End parenthesis to the string.
        Pass it recursively to self with end index incremented by 1.
"""

class Solution:

    def __init__(self):
        self.output_list=[]
        self.count=0

    def get_open_parenthesis(self):
        return '('

    def get_closed_parenthesis(self):
        return ')'

    def recursive_output(self,temp_string="",left_parenthesis=0,right_parenthesis=0):

        if len(temp_string)== 2*self.count:
            #base case
            #you reached the max length, copy it to the output list
            self.output_list.append(temp_string)
            return

        #if the left parenthesis count is less than the specified count, then, add it to temp string
        if left_parenthesis < self.count:
            temp_string+=self.get_open_parenthesis()
            self.recursive_output(temp_string,left_parenthesis+1,right_parenthesis)

        #finish off pairing left parenthesis with right parenthesis
        if right_parenthesis < left_parenthesis:
            temp_string+=self.get_closed_parenthesis()
            self.recursive_output(temp_string,left_parenthesis,right_parenthesis+1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.count=n
        self.recursive_output()
        return self.output_list

sol=Solution()
print(sol.generateParenthesis(10))
