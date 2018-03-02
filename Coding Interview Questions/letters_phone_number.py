"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.


"""
from collections import defaultdict
from collections import deque
"""
Invoke a function passing the digit string and index=0
In that function:
Base case: if index == len-1 then return just the number mapped character array.

output=recurse(number,index+1)
for every curent_char in current number mapped to current character array:
    for every element in the next:
        rewrite the element =current_char +element
return the output
"""

class Solution:
    def __init__(self):
        self.dict_number_to_alphabets=defaultdict(list)
        self.dict_number_to_alphabets={2:['a','b','c'],
                                       3:['d','e','f'],
                                       4:['g','h','i'],
                                       5:['j','k','l'],
                                       6:['m','n','o'],
                                       7:['p','q','r','s'],
                                       8:['t','u','v'],
                                       9:['w','x','y','z']}
        self.output=deque()
        self.converted_list=[]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #prepare a list of all the alphabet combinations
        for index in range(len(digits)):
            number=int(digits[index])
            alphabet_list=self.dict_number_to_alphabets[number]
            if alphabet_list == [] or alphabet_list == None:
                continue
            self.converted_list.append(alphabet_list)
        #start from the end of the list
        for index in range(len(self.converted_list)-1,-1,-1):
            end_list=self.converted_list[index]
            #print(end_list)
            #if the output list is empty, just add the end list to this output list
            if index==len(self.converted_list)-1:
                for char in end_list:
                    self.output.append(char)
            else:
                #dequeue the items from the left of the list.
                #for each item in the output queue, append each character from the previous list and
                #enqueue it back.
                #Repeat this process as you walk forward to the starting of the list.
                #by this way, you will have all the combinations
                total_number_of_items=len(self.output)
                count=0
                while(count<total_number_of_items):
                    output_item=self.output.popleft()
                    #print(output_item)
                    for index2 in range(len(end_list)):
                        new_output_item=end_list[index2]+output_item
                        self.output.append(new_output_item)
                    count+=1
        return self.output

sol=Solution()
print(sol.letterCombinations("23456"))

