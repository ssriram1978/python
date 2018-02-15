#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

from collections import defaultdict

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_container_pairs=defaultdict(str)
        dict_container_pairs={'(':')','{':'}','[':']'}
        isValidString=False
        """
        1. Maintain a stack.
        2. Check if the element is in the dict. If not, push the first element to the stack.
        3. If the element is in the dict, pop the element from the stack and check if they match.
        4. If they do not match, return false.
        5. If they match, then, continue with the next character.
        6. Return the final output.
        """
        #print(dict_container_pairs)
        container_stack=[]
        index=0
        for index in range(len(s)):
            character=s[index]
            #print("Found a character %c"%(character))
            #check if the character is a key
            if character in dict_container_pairs.keys():
                #append the character to the container stack.
                container_stack.append(dict_container_pairs[character])
                #print("Appending %c in the stack"%(dict_container_pairs[character]))
            else:
                # pop an element from the stack and check if they match
                popped_character=""
                if len(container_stack) > 0:
                    popped_character = container_stack.pop()
                #if popped_character =="":
                #    print("Cannot find any end character to match %c"%(character))
                if character == popped_character:
                    #match found
                    #print("Match found %c %c"%(popped_character,character))
                    continue
                else:
                    #no match found
                    #print("No match found for the character %c"%(popped_character))
                    break

        if index == len(s)-1:
            #the whole string matched, return true
            isValidString=True
        #else:
        #    print("index=%d,length=%d"%(index,len(s)))
        return isValidString

sol=Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("()[{]}"))
print(sol.isValid("([)]{}"))
print(sol.isValid("[()]{}"))
print(sol.isValid("{[()]}"))
print(sol.isValid("{}[()]}"))
