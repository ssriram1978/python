"""
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
"""
The basic idea is to find out the smallest result letter by letter (one letter at a time).
Here is the thinking process for input "cbacdcbc":
Find out the last appeared position for each letter; c - 7 b - 6 a - 2 d - 4
Find out the smallest index from the map in step 1 (a - 2);
The first letter in the final result must be the smallest letter from index 0 to index 2;
Repeat step 2 to 3 to find out remaining letters.
The smallest letter from index 0 to index 2: a
The smallest letter from index 3 to index 4: c
The smallest letter from index 4 to index 4: d
The smallest letter from index 5 to index 6: b
So the result is "acdb"
"""
from collections import defaultdict
class Solution:
    def getSortedList(self,s):
        string_list = []
        for index in range(len(s)):
            character = s[index]
            string_list.append((character, index))
        string_char_sorted_list = sorted(string_list, key=lambda x: x[0])
        return string_char_sorted_list

    def getMinIndexForMinChar(self,s,string_list):
        # start the output from the first character in the sorted list
        value = string_list[0]
        first_character = value[0]
        # search for the first character in the original string
        starting_index = s.find(first_character)
        return starting_index

    def PrepareMinString(self,input_string,sorted_list,starting_index):
        hash_table_char=defaultdict(int)
        output_string=""

        for index in range(starting_index,len(input_string)):
            if hash_table_char[input_string[index]]==0:
                #add it to hash table and output string
                hash_table_char[input_string[index]]=1
                output_string+=input_string[index]

        #make sure that you did not miss out any unique non repeating characters before the starting index.
        for index in range(0,starting_index):
            if hash_table_char[input_string[index]]==0:
                #you found a unique character
                #prepend it to the output string
                output_string=input_string[index]+output_string
                hash_table_char[input_string[index]] = 1
                
        return output_string

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s== None or s == "" or type(s)!=str:
            return None
        #get the sorted char list with index.
        string_list=self.getSortedList(s)
        #get the first char and the min index of the first char in s.
        starting_index=self.getMinIndexForMinChar(s,string_list)
        #prepare the string in lexicographic order and return it.
        output=self.PrepareMinString(s,string_list,starting_index)

        return output

s=Solution()

print(s.removeDuplicateLetters("eeeeeeccccccccdddddddda"))
