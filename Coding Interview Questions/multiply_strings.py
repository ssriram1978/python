"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
"""
split the input mum1 and num2 into a list.
Declare an integer variable named output.
Declare a running count = 0
for each character in num1 from the end:
    Compute the integer by subtracting ascii value of '0' from the ascii value of the current digit character.
    Multiply the integer with last character converted to integer of num2.
    If there is a carry, bring it to the next character of num2 and perform the above two steps until you reach
    the beginning of num2.
    Compute the result.
    Left shift the result by running count.
    Add the result to output.

Return output.
"""

class Solution(object):
    def prepare_list(self,num,list_num):
        for character in num:
            list_num.append(character)

    def compute_mult(self,list_num2,single_char):
        first_int = ord(single_char) - ord('0')
        carry=0
        iteration=0
        result=0
        for index in range(len(list_num2)-1,-1,-1):
            second_int=ord(list_num2[index]) - ord('0')
            mult_result=first_int*(second_int)+ carry
            print("mult_result=%d"%(mult_result))
            if index != 0 and mult_result > 9:
                #if you reached the beginning, No need to compute carry
                #take the carry to the next digit
                carry=mult_result//10
                digit=mult_result%10
            else:
                digit=mult_result
            #store the digit
            result+=digit*(10**iteration)
            iteration+=1
        return result

    def compute_product(self,list_num1,list_num2):
        # multiply one list within another.
        # declare a running count initialized to 0
        running_count = 0
        #declare an output variable initialized to 0
        output=0
        for index in range(len(list_num1) - 1, -1, -1):
            single_char=list_num1[index]
            # use this current_int to multiply the list_num2
            compute=self.compute_mult(list_num2,single_char)
            #left shift compute by running count and add it to output
            print("compute %c * "%(single_char) + str(list_num2)+"Returned %d"%(compute))
            output+=compute*(10**running_count)
            running_count+=1
        return output

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if type(num1) != str or type(num2) != str or len(num1)==0 or len(num2)==0:
            return ""
        #declare an output variable initialized to 0
        output=0
        #prepare two lists list_num1 and list_num2
        list_num1=[]
        self.prepare_list(num1,list_num1)
        list_num2 = []
        self.prepare_list(num2, list_num2)
        output=self.compute_product(list_num1,list_num2)
        #prepare output as a string and return it.
        return str(output)

sol=Solution()
print(sol.multiply("123","456"))

print(123*456)
