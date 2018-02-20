"""
1.6 String compression
Implement a method to perform basic string compression using the counts of repeated characters.
 For example, the string aabccccaaa would become a2b1c4a3.
If the compressed string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).
"""

def compress_string(string_val):
    #initialize the compressed string to empty
    compressed_string=""
    #define a variable that will be used as an index into the original string.
    index=0
    #start a while loop to iterate over each and every character in the original string.
    while(index < len(string_val)):
        #fetch the character from the original string at the desired location.
        character=string_val[index]
        #append the character to the compressed string.
        compressed_string+=character
        #Define a count variable to count the number of times the character is repeated in the original string.
        count=0
        #start a while loop to keep incrementing the index and count as long as
        # current index is less than the length of the string
        #character at current index is equal to the character at the next index.
        while(index < len(string_val) and
            character == string_val[index]):
            index+=1
            count+=1
        #append the final count to the compressed string.
        compressed_string +=str(count)

    if len(compressed_string) < len(string_val):
        return compressed_string
    else:
        return string_val

print(compress_string("abca"))

