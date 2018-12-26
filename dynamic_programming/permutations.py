"""
Print all the permutations of a string.
"sriram"

s + riram irram rriam
    r + iram riam airm mira
        i + ram mar amr
            r + am ma
                a + m
1. Split the string and recurse and then join the string.
"""


def permutations_recurse(input_str):
    if not input_str:
        return [""]
    output = []
    for index in range(len(input_str)):
        remaining_string = input_str[:index] + input_str[index+1:]
        output += [input_str[index] + x for x in permutations_recurse(remaining_string)]
    return output

def permutations_of_a_string(input_str):
    return permutations_recurse(input_str)

def factorial(number):
    total = 1
    for index in range(1, number+1):
        total *= index
    return total

input="Sriram"
permutation_list = permutations_of_a_string(input)
print("Permutation of {} is {}".format(input,
                                       permutation_list))
"""
permutation of picking all the characters, order is important and without repetition.
nPr = n!/(n-r)!
"""

print("total number of permutations = {}, length of output={}"
      .format(factorial(len(input)), len(permutation_list)))
