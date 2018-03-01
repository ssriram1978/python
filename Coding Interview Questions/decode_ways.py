"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

1234
"""

"""
This problem can be solved recursively and non recursively.

Recursive solution:
--------------------
Given an input string:
Declare final_computed_answer=0
Recurse until you reach the end character of the string.
If  you have just one character of the string,
    return 1 back to the recursive call.
Else
    compute if current character combined with current character +1 < 26,
     then final_computed answer = 2 + result of the recursive call.
return the final_computed_answer back to the calling function.
"""

class Solution:
    def decode_ways_recurse(self,input_string,start):
        if input_string == None or len(input_string)==0 or type(input_string)!=str:
            return 0
        if start==len(input_string)-1:
            return 1
        else:
            count=1
            integer_number=input_string[start]+input_string[start+1]
            integer_number=int(integer_number)
            if integer_number >=10 and integer_number <=26:
                count+=1
            count+=self.decode_ways_recurse(input_string,start+1)
        return count

    def numDecodings(self,input_string):
        if input_string == None or len(input_string)==0 or type(input_string)!=str:
            return 0
        return self.decode_ways_recurse(input_string,0)

sol=Solution()
print(sol.numDecodings("123"))
