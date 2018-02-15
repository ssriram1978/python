"""
convert an integer into binary form by invoking bin() and convert it into a string.
Get rid off the 0b in front of the string to get the number in full binary form.
start from the beginning and keep swapping pair of bits.
return the output.
"""
def pairwise_bit_swap(input_number):
    if input_number == None:
        return
    input_string = str(bin(input_number))
    input_list = list(input_string[2:])

    for index in range(0,len(input_list)-1,+2):
        temp=input_list[index]
        input_list[index]=input_list[index+1]
        input_list[index+1]=temp

    print("Before pairwise bitswap input=" + str(bin(input_number)))
    output_string=''.join(input_list)
    print("After pairwise  bitswap output=" + (output_string))

    output_string="0b"+output_string
    output=int(output_string,2)
    print("output in binary="+ str(bin(output)))
    return output

pairwise_bit_swap(0b1010)
pairwise_bit_swap(0b0101)
