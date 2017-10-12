#chapter 1 solutions

from operator import *


# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def check_for_unique_characters_in_string(stringcheck):
    if (stringcheck == None or len(stringcheck) == 0):
        print("input string is null")
        return 0

    dictionary = {}
    for index in range(len(stringcheck)):
        object = dictionary.get(stringcheck[index])
        if object != None:
            # print("object is not null" + stringcheck[index])
            return 0
        else:
            # print("Adding object " + stringcheck[index] + " to dict")
            dictionary[stringcheck[index]] = 1
    return 1


print("check for all unique characters in the string returned %d " % (check_for_unique_characters_in_string("abcwdf")))


# Implement a function void reverse(char* str) in C or C++ which reverses a nullterminated string.
def swap_alphabets_from_a_sentence(sentence):
    if (sentence == None):
        return 0

    output_sentence = ""
    for index in range(len(sentence) - 1, -1, -1):
        output_sentence += sentence[index]

    return output_sentence


print("swapped o/p=" + swap_alphabets_from_a_sentence("Hello world"))


# Given two strings, write a method to decide if one is a permutation of the other.
def check_if_one_string_is_permutation_of_other(string1, string2):
    # create a name value pair for string1
    dictionary1 = {}
    for index in range(len(string1)):
        if dictionary1.get(string1[index]) == None:
            dictionary1[string1[index]] = 1
        else:
            object = dictionary1[string1[index]]
            object += 1
            dictionary1[string1[index]] = object

    # create a name value pair for string2
    dictionary2 = {}
    for index in range(len(string2)):
        if dictionary2.get(string2[index]) == None:
            dictionary2[string2[index]] = 1
        else:
            object = dictionary2[string2[index]]
            object += 1
            dictionary2[string2[index]] = object

    #print(dictionary1)
    # make sure that name value pair of string1 is present in string2.
    for name, value in dictionary1.items():
        if dictionary2.get(name) == None or dictionary2.get(name) != value:
            return 0

    #print(dictionary2)
    # make sure that name value pair of string1 is present in string2.
    for name, value in dictionary2.items():
        if dictionary1.get(name) == None or dictionary1.get(name) != value:
            return 0
    return 1


print("check_if_one_string_is_permutation_of_other returned %d" % (check_if_one_string_is_permutation_of_other('sriram','mriras')))


# Write a method to replace all spaces in a string with'%20'.
# You may assume that the string has sufficient space at the end of the string to hold the additional characters,
# and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character
# array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith
# Output: "Mr%20Dohn%20Smith"


def replace_all_spaces_with_string(input_string):
    output_string=""
    for index in range(len(input_string)):
        if(input_string[index] == " "):
            output_string+="%20"
        else:
            output_string +=input_string[index]
    return output_string

print("replace_all_spaces_with_string returned %s" %(replace_all_spaces_with_string("sriram    sridhar")))


# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.

def perform_string_compression(input_string):
    compressed_string=""
    dictionary={}
    for index in range(len(input_string)):
        object=dictionary.get(input_string[index])
        if(object == None):
            dictionary[input_string[index]]=1
        else:
            object+=1
            dictionary[input_string[index]]=object

    sorted_dictionary=sorted(dictionary.items(),key=itemgetter(0),reverse=False)

    for name,value in sorted_dictionary:
        compressed_string+=name
        compressed_string+=str(value)

    if(len(compressed_string) > len(input_string)):
        return input_string
    else:
        return compressed_string

print("perform_string_compression returned " + perform_string_compression("sriramsridharhomeaeopfuaeopfuaepfuapaeifjaefaeifhaeoifaeiof"))



# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?



# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.



# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubstring
# (e.g.,"waterbottle"is a rotation of "erbottlewat")

def isSubstring(concat_string,checked_string):
    if(concat_string == None or checked_string == None):
        return 0
    if(checked_string in concat_string):
        return 1
    else:
        print("no match found")
        return 0

def check_for_word_rotation(original_string, checked_string):
    if(original_string == None or checked_string == None):
        return 0
    concat_string=original_string
    concat_string+=original_string
    return isSubstring(concat_string,checked_string)

print("check_for_word_rotation returned {:d}".format(check_for_word_rotation("sriram", "amsrir")))

