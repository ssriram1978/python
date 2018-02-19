"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.

"""
"""
Algorithm:
----------
Perform a BFS (Breadth First Search) on the wordlist by searching the beginword with each word in the wordlist.
Enqueue the beginword into the wordlist and increment a counter by 1.
Start a while loop that iterates while the list is not empty:
    In this while loop, do the following.
    Dequeue the current_word from the queue.
    Peform a sweep of the dictionary of words to find a word in the dictionary that differ
    by one single character with the current_word.
        If you found a match, then, 
            Enqueue that word to the queue.
            Increment the match by 1
            Delete the word from the dictionary so that you don't reuse it again.
            If the word matches with the endword, then, break from the while loop and return the current match count.
        If you did not find a match, then,do nothing.
"""
from collections import defaultdict
from collections import deque

class Solution(object):
    def isAdjacent(self,word1,word2):
        #return True if word1 differs utmost by 1 character when compared with word2

        if len(word1) != len(word2):
            return False

        character_difference=0
        isAdjacent=False
        for index in range(min(len(word1),len(word2))):
            if word1[index] != word2[index]:
                character_difference+=1
            if character_difference >1:
                #break from for loop
                break
        if character_difference == 1:
            isAdjacent=True
        return isAdjacent

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #keep a copy of the words that matched with the current word
        matched_adjacent_words=[]
        #create a temporary queue that is used for BFS enqueue/dequeue operation.
        queue_bfs=deque()
        #create a default dict to store the words in wordlist to avoid multiple iterations.
        word_dict=defaultdict(int)
        #enqueue the first word into queue_bfs
        queue_bfs.append(beginWord)
        matched_adjacent_words.append(beginWord)
        #declare a boolean variable that is used to break from the while loop
        end_word_found=False
        while len(queue_bfs) > 0:
            #dequeue the element.
            word=queue_bfs.popleft()
            print("word to be searched is=%s."%(word))
            #declare a temp_list which captures all the adjacent words in one sweep
            temp_list=[]
            #search if the word is adjacent with any of the words in the dictionary.
            for index in range(len(wordList)):
                if word_dict[wordList[index]]==1:
                    #skip this word as it was already processed.
                    continue
                if self.isAdjacent(word,wordList[index])==True:
                    #Increment the count by 1.
                    print("Found adjacent word=%s for word=%s"%(wordList[index],word))
                    if wordList[index] == endWord:
                        #match found
                        matched_adjacent_words.append(endWord)
                        end_word_found=True
                        break
                    else:
                        #append the words to temp_list
                        temp_list.append(wordList[index])
                        # equivalent of marking visited node as True
                        word_dict[wordList[index]]=1

            if end_word_found == True:
                print(matched_adjacent_words)
                break
            else:
                for word in temp_list:
                    #append the list of words to the queue_bfs
                    queue_bfs.append(word)
                    # add the dictionary word to matched_adjacent_words,queue_bfs
                    matched_adjacent_words.append(word)
                    break

        return len(matched_adjacent_words)

sol=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print("is adjacent %s %s returned %s"%(beginWord,endWord,str(sol.ladderLength(beginWord,endWord,wordList))))
wordList = ["hot","dot","lot","dog","log","cog"]
print("is adjacent %s %s returned %s"%(beginWord,endWord,str(sol.ladderLength(beginWord,endWord,wordList))))
