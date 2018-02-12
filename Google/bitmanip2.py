#you have an integer and you can flip exactly one bit from 0 to 1.
#find the length of the longest sequence of 1s that you can create
#example: Input: 1775 (or: 11011101111)
#output 8
"""
Convert the number to ascii. bin(output)
Starting from index 0 keep looking for a character with 0 and while looking for 0
    keep incementing the number of 1's in that string.
Once you reached 0 mark that location and keep looking for the next 0 in the string and while looking for 0
    keep incrementing the number of 1's in that string.
Store the max number of 1's in a max variable if the previously computed max variable is less than the current max number of 1's.

Keep repeating the above said step from the marked location till the end of the string.
Return the max variable.
"""

def find_longest_seq_of_1s(input):
    if input == None:
        return None
    #convert the integer into a string
    input_bit_string=str(bin(input))
    #get rid off the 0b at the beginning of the string
    input_bit_string=input_bit_string[2:]
    #declare longest_sequence=0
    longest_sequence=0
    #declare a variable that is used to count the 1s in the string until the next 0
    number_of_one_in_string=0
    #start a for loop that identifies zeros in the string
    for index in range(len(input_bit_string)):
        if input_bit_string[index] == '1':
            number_of_one_in_string+=1
        elif input_bit_string[index] == '0':
            number_of_one_in_string += 1
            #starting from the next index try to find all ones until next 0
            for index2 in range(index+1,len(input_bit_string)):
                if input_bit_string[index2]=='1':
                    number_of_one_in_string += 1
                elif input_bit_string[index2]=='0':
                    break
            if index2 == len(input_bit_string):
                #you already reached the end, break from outer for loop
                break
            #store the number_of_one_in_string as longest sequence
            if longest_sequence < number_of_one_in_string:
                longest_sequence = number_of_one_in_string
            #reset the number_of_one_in_string to 0
            number_of_one_in_string=0

    #take into account the corner edge cases
    if longest_sequence < number_of_one_in_string:
        longest_sequence=number_of_one_in_string


    return longest_sequence

print(find_longest_seq_of_1s(int(0b111011101111)))

