"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    52 -> AZ
    53 -> AAA
Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC
AAA=27+26=53
AAAA=53+26

52=26*1+26->AZ
702=26*26+26->ZZ
"""
"""
To convert integer to title:
    If the integer is less than or equal to 26, then send the character back to the recursive call.
    Else:
    character_str=""
    difference=integer-26
    character_str+=recursive(difference)
    Now compute the quotient=difference%26 and convert quotient to a character and append it to character_str.
return character_str

To convert title back to integer can be easily solved via recursion.
Recurse till the end of the string.
If you have just one element in the string:
    return the integer value of the element back to the recursive call.
Else:
    Get the integer value of the current element.
    Multiply it by 26 and add the result with the recursive call to the output.
return output
"""

class Solution(object):
    def convert_number_to_character(self,number):
        return chr(ord('A')+(number-1))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0 or type(n) != int:
            return ""
        if n>1 and n <=26:
            return self.convert_number_to_character(n)
        else:
            character_array=""
            num=(n//26)
            #append the character
            character_array+=self.convertToTitle(num)
            character_array=self.convert_number_to_character(num)+character_array
        return character_array

    def convert_character_to_number(self,character):
        return ord(character)-ord('A')+1

    def convertTitleToNumberRecurse(self,title,start):
        if start == len(title)-1:
            return self.convert_character_to_number(title[start])
        else:
            count = 0
            count=self.convert_character_to_number(title[start])
            count=count*26+self.convertTitleToNumberRecurse(title,start+1)
        return count

    def convertTitleToNumber(self,title):
        if title==None or len(title)==0 or type(title) != str:
            return 0
        return self.convertTitleToNumberRecurse(title,0)

sol=Solution()
print(sol.convertToTitle(28))
print(sol.convertTitleToNumber("AA"))
print(sol.convertTitleToNumber("AZ"))
print(sol.convertTitleToNumber("ZZ"))
print(sol.convertTitleToNumber("ZZZ"))
