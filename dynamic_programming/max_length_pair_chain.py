"""
You are given n pairs of numbers.
In every pair, the first number is always smaller than the second number.
Now, we define a pair (c,d) can follow another pair (a,b) if and only if
b < c. Chain of pairs can be formed in this fashion.
Given a set of pairs, find the length of the longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.
Example:
    Input [[1,2],[2,3],[3,4]]
    output : 2
    Explanation: The longest chain is [1,2] -> [3,4]
"""

def find_longest_pair_chain(input):
    if len(input) == 0:
        return 0
    dp = [0] * len(input)
    input = sorted(input, key=lambda x: x[0]) #O(n *log(n))
    for index in range(len(input)): #O(n**2)
        dp[index] = 1
        #look back and find the maximum chain that could be formed from the current location.
        for index2 in range(index - 1, -1, -1):
            if input[index2][1] < input[index][0]:
                dp[index] = max(dp[index],
                                1 + dp[index2])
    print(dp)
    return dp[-1]


input=[[1,2],[2,3],[3,5],[4,5],[4,5],[4,6],[5,7],[11,15], [16,18]]
print("Longest possible pair chain is {}.".format(find_longest_pair_chain(input)))