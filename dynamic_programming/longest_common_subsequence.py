"""
Given two sequences X[1..m] and Y[1..n], find the longest common subsequence between them.
Example:
    X: ABAC BDAB
    Y: BDCAB A
    Longest common subsequence: BCBA

"""


def lcs_recurse(X,Y,m,n,dp):
    if m == 0 or n == 0:
        return 0
    if dp[m-1][n-1]:
        return dp[m-1][n-1]

    if X[m-1] == Y[n-1]:
        dp[m - 1][n - 1] = 1 + lcs_recurse(X,Y,m-1,n-1,dp)
        return dp[m - 1][n - 1]
    else:
        dp[m - 1][n - 1] = max(lcs_recurse(X,Y,m,n-1,dp),
                               lcs_recurse(X, Y, m - 1, n, dp))
        return dp[m - 1][n - 1]


def lcs(X,Y,m,n):
    dp=[[0 for x in range(m)] for y in range(10000)]
    return lcs_recurse(X,Y,m,n,dp)


def longestCommonSubSequenceRecurse(str1, str2, cache, str1_index, str2_index):
    # base case
    if str1_index == 0 or str2_index == 0:
        return ""

    if str1[str1_index-1] == str2[str2_index-1]:
        # Take the matching character out
        # append the matching character with the LCS of the remaining characters in str1 and str2.
        if len(cache[str2_index][str1_index]):
            return cache[str2_index][str1_index]

        cache[str2_index][str1_index] += longestCommonSubSequenceRecurse(str1,
                                                                         str2,
                                                                         cache,
                                                                         str1_index-1,
                                                                         str2_index-1)
        cache[str2_index][str1_index] += str2[str2_index-1]
        return cache[str2_index][str1_index]
    else:
        # Return the max string length of cache[str1_index-1][str2_index] and
        # cache[str1_index][str2_index-1]
        if str1_index - 1 < 0 and str2_index-1 < 0:
            # row 0 and column 0, return ""
            return ""
        elif str1_index-1 < 0:
            # you are at column 0.Return the value found at the row above the current row.
            if not len(cache[str2_index - 1][str1_index]):
                cache[str2_index - 1][str1_index] = longestCommonSubSequenceRecurse(str1,
                                                                                    str2,
                                                                                    cache,
                                                                                    str1_index,
                                                                                    str2_index - 1)
            return cache[str2_index - 1][str1_index]
        elif str2_index-1 < 0:
            # you are at the top row. Return the value found to the left column of the current row.
            if not len(cache[str2_index][str1_index - 1]):
                cache[str2_index][str1_index - 1] = longestCommonSubSequenceRecurse(str1,
                                                                                    str2,
                                                                                    cache,
                                                                                    str1_index - 1,
                                                                                    str2_index)
            return cache[str2_index][str1_index-1]

        # populate the interested row and columns in cache if they are not already filled in.
        if not len(cache[str2_index][str1_index-1]):
            cache[str2_index][str1_index - 1] = longestCommonSubSequenceRecurse(str1,
                                                                                str2,
                                                                                cache,
                                                                                str1_index-1,
                                                                                str2_index)
        if not len(cache[str2_index-1][str1_index]):
            cache[str2_index-1][str1_index] = longestCommonSubSequenceRecurse(str1,
                                                                              str2,
                                                                              cache,
                                                                              str1_index,
                                                                              str2_index-1)
        # return the max string which is found
        if len(cache[str2_index][str1_index-1]) > len(cache[str2_index-1][str1_index]):
            # print("{} is greater than {}.".format(cache[str2_index][str1_index-1],
            #                                      cache[str2_index - 1][str1_index]))
            return cache[str2_index][str1_index-1]
        elif len(cache[str2_index][str1_index-1]) < len(cache[str2_index-1][str1_index]):
            # print("{} is lesser than {}.".format(cache[str2_index][str1_index-1],
            #                                      cache[str2_index - 1][str1_index]))

            return cache[str2_index-1][str1_index]
        else:
            # print("{} is Equal to {}.".format(cache[str2_index][str1_index-1],
            #                                      cache[str2_index - 1][str1_index]))

            return cache[str2_index][str1_index - 1]

def longestCommonSubsequence(str1, str2):
    # Write your code here.
    #prepare a two dimensional array that stores a list of characters at each location.
    cache = [[[] for y in range(len(str1)+1)]  for x in range(len(str2)+1)]
    #invoke a recursive function to compute and store the longest common subsequence.
    return longestCommonSubSequenceRecurse(str1, str2, cache, len(str1), len(str2))


def longestCommonSubsequenceNonRecurse(str1, str2):
    # prepare a two dimensional array that stores a list of characters at each location.
    cache = [[[] for y in range(len(str1) + 1)] for x in range(len(str2) + 1)]
    for str2_index in range(1, len(str2)+1):
        for str1_index in range(1, len(str1)+1):
            if str1[str1_index-1] == str2[str2_index-1]:
                cache[str2_index][str1_index] += cache[str2_index-1][str1_index-1] + [str1[str1_index-1]]
            else:
                cache[str2_index][str1_index] = max(cache[str2_index][str1_index-1],
                                                    cache[str2_index-1][str1_index],
                                                    key=len)
    return cache[-1][-1]

X="8aaaaaaaaaa1aaaaaaaaaaaa4233333333333333333"
Y="234555567777777777777777777777777777777777777777777777"
#print("longest common subsequence length={}".format(lcs(X,Y,len(X),len(Y))))

print("longest common subsequence ={}".format(longestCommonSubsequenceNonRecurse(X,Y)))


print(float("-inf"))