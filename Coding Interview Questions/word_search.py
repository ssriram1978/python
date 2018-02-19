"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
"""
Iterative algorithm:
---------------------
DFS (Depth First Search) This is the way to go because
For every search, backtracking is needed because every path and every combination need to be
analyzed for a possible match.
Example: string "abc" matched successfully but the next character did not match. In this case,
We need to find the last character in the neighborhood of the previous character and continue the search.
In this example, we need to find "c" in the neighborhood of "b" and continue the search.
This falls under Depth first search algorithm where the algorithm tries to invoke recursively until it finds
a match deep into the tree and then search for neighbors surrounding the parent node until it reaches the root.
"""
from collections import defaultdict

class Solution(object):
    def search_word_in_board(self,board,word,word_index,row,column):

        #base case.
        if board == None or word == None:
            return []
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or word_index >= len(word):
            return []

        #define a temporary array to capture all the characters found.
        char_found_list = []

        #check if the character at the current location in the word matches with the character at the given location in the board.
        if word[word_index] == board[row][column]:
            #match found
            print("Character match %c found."%(word[word_index]))
            char_found_list.append(word[word_index])
            #since the same board character cannot be looped back again, mask the character to say $
            #this is for the check to fail when the same character on the board is looked up.
            temp_storage=board[row][column]
            board[row][column]='$'
            #move to the next character
            if word_index==len(word)-1:
                #you reached the end
                print("You reached the end. Complete match found.")
                return char_found_list
            else:
                char_list=[]
                print("Searching for the char %c on the right side of the board" % (word[word_index + 1]))
                #search for the next character in the word on the right side of the current character in board
                char_list=self.search_word_in_board(board,word,word_index+1,row,column+1)
                if char_list == []:
                    print("Searching for the char %c on the left side of the board" % (word[word_index + 1]))
                    # search for the next character in the word on the left side of the current character in board
                    char_list=self.search_word_in_board(board,word,word_index+1,row,column-1)
                    if char_list == []:
                        print("Searching for the char %c on the top of the board" % (word[word_index + 1]))
                        # search for the next character in the word on the top of the current character in board
                        char_list=self.search_word_in_board(board,word,word_index+1,row-1,column)
                        if char_list == []:
                            print("Searching for the char %c on the bottom of the board" % (word[word_index + 1]))
                            # search for the next character in the word on the bottom of the current character in board
                            char_list=self.search_word_in_board(board,word,word_index+1,row+1,column)
                #check if the char_list is empty
                if char_list == []:
                    #reset the char_found_list to []
                    print("No match found, resetting the list to empty")
                    char_found_list=[]
                    #remember to restore the temp char mask to original value
                    board[row][column] = temp_storage
                    return char_found_list
                else:
                    #append the char list to the original char_found_list
                    print("appending" + str(char_list) + "to the original list" + str(char_found_list))
                    char_found_list.extend(char_list)
                    print(char_found_list)
                    # remember to restore the temp char mask to original value
                    board[row][column] = temp_storage
                    return char_found_list
        else:
            char_found_list=[]
            return char_found_list


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        char_found_list=[]
        match_found=False
        for row in range(len(board)):
            for column in range(len(board[0])):
                char_found_list = self.search_word_in_board(board, word, 0, row, column)
                if char_found_list != []:
                    print("Returning " + str(char_found_list))
                    match_found=True
                    break
            if match_found==True:
                break

        if match_found==False:
            return False
        else:
            print(char_found_list)
            return True



board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
sol=Solution()
print("Search for BCESCEE returned "+ str(sol.exist(board,"BCESCEE")))
print("Search for BCESCEES returned "+ str(sol.exist(board,"BCESCEES")))

"""
Non iterative algorithm:

It is fully not ready because backtracking needs to be accounted for.

For every character in board, perform the following:
    Peform a linear search for the occurance of the first character in the board:
        If you find the first character, mark the location of the character (x,y)
                where x is the index of the row.
                where y is the index of the column.
            Store these indexes in a board_dict where the character is the key.

Declare is_match_found to be False
Declare character_index to be 0
Declare previous_character list to be []
While is_match_found==False or character_index reached the end of the character, do the following:
    Find the list of character occurances from the board_dict.
        If this is the first character then, 
            Store the first character in word_list with the list of occurances.
        Else:
            Declare a boolean flag current_character_match and set it to False 
            For every occurance of the character (a,b) from the list:
                Iterate over every occurance of the last character(x,y) from word_list:
                Check if one of the following condition match occurs:
                    1. right match x,y+1 == a,b
                    2. down match x+1,y == a,b
                    3. left match x,y-1 == a,b
                    4. up match, x-1,y == a,b
                    If one of these above said conditions match,
                        set current_character_match to True.
                        Append this current_character match to the word_list.
                        Continue the search and if you find one more match append this to the word_list
            if current_character_match is True:
                store the current character index as previous_character index
                if you already reached the end of the word, then set the is_match_found to True
            else:
                Go back to the previous character and search for the next character in the neighborhood
                of the previous character.
                This requires backtracking and a flag that denotes whether the previous character list is searched 
                fully or not. 

return is_match_found
"""