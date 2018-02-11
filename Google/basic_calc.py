"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
(1*(3*(2/(5+3*4))+10*(1/(3*4))))
"""


class Solution:
    def isNumber(self,ch):
        if ord(ch) >=48 and ord(ch) <=57:
            return True
        else:
            return False

    def isAddition(self,ch):
        if ch=="+":
            return True
        else:
            return False

    def isSubtraction(self,ch):
        if ch=="-":
            return True
        else:
            return False

    def isMultiplication(self,ch):
        if ch=="*":
            return True
        else:
            return False

    def isDivision(self,ch):
        if ch=="/":
            return True
        else:
            return False
    def isAddSubMultDiv(self,ch):
        if self.isAddition(ch) or self.isSubtraction(ch) or self.isMultiplication(ch) or self.isDivision(ch):
            return True
        else:
            return False

    def isOpenParenthesis(selfself,ch):
        if ch=="(":
            return True
        else:
            return False

    def isClosedParenthesis(selfself,ch):
        if ch=="/":
            return True
        else:
            return False

    def compute(self,number,sign,result):
        int_number=0
        computed_result=result
        print("number=%d" % (int_number)+"sign="+sign+" and result=%d"%(result))
        if number != "":
            int_number=int(number)
        else:
            print("Invalid number "+number)

        # compute the previous result
        if self.isAddition(sign):
            computed_result += int_number
        elif self.isSubtraction(sign):
            computed_result -= int_number
        elif self.isMultiplication(sign):
            computed_result *= int_number
        elif self.isDivision(sign):
            computed_result /= int_number
        print("computed result="+str(computed_result))
        return computed_result

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==None or s=="":
            return 0
        s=''.join(s.split())
        print("You entered"+s)
        #convert string to list (stack)
        #self.convert_string_to_list(s)
        number=""
        sign=""
        result=0
        calc_stack=[]
        for index in range(0,len(s),1):
            character=s[index]
            print("Extracted character="+character)
            if self.isNumber(character):
                number=character
            elif self.isAddSubMultDiv(character):
                #compute result
                if sign=="":
                    #this is the first time that you encountered a character
                    #store the sign
                    sign=character
                result=self.compute(number,sign,result)
                #clear the previous number
                number=0
                # store this symbol in sign
                sign=character
            elif self.isOpenParenthesis(sign):
                #push the computed result to stack
                calc_stack.append(str(result))
                #push the previous sign to stack
                #reset the result to 0
                result=0
                calc_stack.append(sign)
            elif self.isClosedParenthesis(sign):
                #compute result
                result=self.compute(number,sign,result)
                # clear the previous number by overwriting result with number
                number = result
                #pop the sign and store it in sign
                sign=calc_stack.pop()
                #pop the previous computed result and store it in result
                result=calc_stack.pop()

        #finally compute the result with the left overs
        result=self.compute(number,sign,result)
        return result

sol=Solution()
#print(sol.calculate("1+(4+5+2)-3+(6+8)"))
print(sol.calculate("(1*(4+5+2))-3+(6/8)"))
