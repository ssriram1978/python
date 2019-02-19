"""
Grey code is a binary code where each successive value differ in only one bit,
as well as when wrapping around.
Grey code is common in hardware so that we don't see temporary spurious values during transitions.
Given a number of bits n, generate a possible gray code for it.
For example: for n = 2, one gray code would be [00, 01, 10, 11, 10].
"""

def swap_0_with_1_at_index(grey_code, index):
    swap_bit = None
    if grey_code[index] == '0':
        swap_bit = '1'
    else:
        swap_bit = '0'
    return grey_code[:index] + swap_bit + grey_code[index+1:]

def generate_grey_code(n):
    grey_code_list = []
    if n == 0:
        return grey_code_list
    
    first_grey_code = '0'
    #prepare the first grey code with all 0's upto the desired length.
    for __ in range(n-1):
        first_grey_code += '0'

    #append this to the output list.
    grey_code_list.append(first_grey_code)

    last_grey_code =  None

    #perform a while loop until the last grey code generated element is not
    #equal to the first grey code generated element which has all 0's in it.
    current_index = n-1
    current_grey_code = None
    while last_grey_code != first_grey_code:
        if not last_grey_code:
            last_grey_code = first_grey_code
        current_grey_code = swap_0_with_1_at_index(last_grey_code, current_index)
        if current_grey_code == first_grey_code:
            break
        else:
            grey_code_list.append(current_grey_code)
        last_grey_code = grey_code_list[-1]
        current_index -=1
        #loop current_index from n-1 to 0.
        if current_index == -1:
            current_index = n-1
    return grey_code_list

for index in range(10):
    print("Possible grey codes for n={} is {}.".format(index, generate_grey_code(index)))
