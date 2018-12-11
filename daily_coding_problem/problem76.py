"""
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.

"""
from typing import List


def check_invalid_column(input_array_of_characters, column_index):
    is_invalid = False
    for index in range(len(input_array_of_characters)):
        if index == 0:
            continue
        if input_array_of_characters[index][column_index] < input_array_of_characters[index-1][column_index]:
            is_invalid = True
            break
    return is_invalid


def count_invalid_columns(input_array_of_characters):
    columns = len(input_array_of_characters[0])
    invalid_columns = 0
    for index in range(columns):
        if check_invalid_column(input_array_of_characters, index):
            invalid_columns += 1
    return invalid_columns


input_array_of_characters: List[str] = ['zyx', 'wvu', 'tsr']
print(count_invalid_columns(input_array_of_characters))
