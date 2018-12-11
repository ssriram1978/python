"""

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

"""


class Nodes:
    def __init__(self,value):
        self.value = value
        self.neighbors = []


def add_element_to_a_tree(tree, element):
    longest_sub_sequence = 0

    if tree.value < element:
        for tree_elements in tree.neighbors:
            longest_sub_sequence = max(longest_sub_sequence, 1 + add_element_to_a_tree(tree_elements, element))
        print("At {}, appending {} to its neighbors".format(tree.value, element))
        tree.neighbors.append(Nodes(element))
        longest_sub_sequence = max(2, longest_sub_sequence)
        print("At {}, the longest is {}".format(tree.value, longest_sub_sequence))
    return longest_sub_sequence


def longest_increasing_subsequence(input):
    longest_sub_sequence = 0
    tree = None
    for element in input:
        if not tree:
            tree = Nodes(element)
            continue
        else:
            longest_sub_sequence = max(longest_sub_sequence, add_element_to_a_tree(tree, element))
            print("After insering {}, the longest is {}".format(element, longest_sub_sequence))
    return longest_sub_sequence


input=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(input))
