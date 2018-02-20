"""
Write a python module to return the number of unmatched characters between two input strings.
Example:
    string1 = abcdefgh
    string2 = abcghij
    unmatched count= 5 (def ij)

#>>> unmatched_alphabet_count("abcdefgh","abcghij")
5
"""

"""
Algorithm:
----------
Create a dictionary for the first string with key as each character in the string and value as the count.
Declare unmatched_count to be 0
For every character in the second string:
    Check if the character is present in the dictionary:
        If it is not present, then increment a unmatched_count by 1
        Else
        Delete the element from the dictionary
return unmatched_count+length of dictionary
        
"""
from collections import defaultdict

def unmatched_alphabet_count(a, b):
    unmatched_count=0
    dictionary_of_char_from_a=defaultdict(int)
    for character in a:
        dictionary_of_char_from_a[character]+=1
    for character in b:
        if dictionary_of_char_from_a[character] <= 0:
            unmatched_count+=1
            #for a defaultdict when you search for an element,
            # it automatically adds the element with index 0 if the item is not there in the dict.
            del dictionary_of_char_from_a[character]
        else:
            del dictionary_of_char_from_a[character]

    print(dictionary_of_char_from_a)
    print(unmatched_count)
    return unmatched_count + len(dictionary_of_char_from_a)


#a = input().strip().split(' ')
#b = input().strip().split(' ')

#a = input().strip()
#b = input().strip()

print(unmatched_alphabet_count("abcdefgh","abcghij"))

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
