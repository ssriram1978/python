"""
Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 2**2 + 3**2 = 9 + 4 = 13
Given n = 27, return 3 since 27 = 3**2 + 3**2 + 3**2 = 9+9+9
"""

from math import sqrt


def find_smallest_number_of_squared_integers_sum_upto_n(integer_num):
    """
    Algorithm:
    ----------
    1. If the integer_num is 1 return 1 because 1**2 is 1.
    2. Find the square root of integer_num as X.
    3. If X is integer, then return 1.
    4. Else:

            Compute the recursive fn called output which should return the total number of
            squares of sub numbers that add up to the current number - square of the integer part of X.

            Y = find_smallest_number_of_squared_integers_sum_upto_n(integer_num - int(X**2))
            if not Y:
                #You could not find any squares that add up to the current number.
                return 0
            else:
                return Y+1 # You need to account for the current number int(x)

    :param integer_num:
    :return:
    """
    # corner case.
    if integer_num == 0:
        return 0
    elif integer_num == 1:
        return 1

    x = sqrt(integer_num)
    # return 1 if the integer num can be split into two perfect squares.
    if x.is_integer():
        return 1
    else:
        # recurse to find the squares of integer_num - x**2
        y = find_smallest_number_of_squared_integers_sum_upto_n(integer_num - int(x)**2)
        # if you found a non zero value, then increment the total count by 1 to account for x as well.
        if y:
            y += 1
        return y


for index in range(10,20):
    print("find_smallest_number_of_squared_integers_sum_upto_{} returned {}"
    .format(index, find_smallest_number_of_squared_integers_sum_upto_n(index)))


