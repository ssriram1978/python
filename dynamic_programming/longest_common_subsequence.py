"""
Given two sequences X[1..m] and Y[1..n], find the longest common subsequence between them.
Example:
    X: ABAC BDAB
    Y: BDCAB A
    Longest common subsequence: BCBA

"""


def longest_common_subsequence_recurse(X, Y, m, n, dp, dp_string):
    if m == 0 or n == 0:
        return 0

    if X[m-1] == Y[n-1]:
        if dp[m-1][n-1] == -1:
            dp[m-1][n-1] = longest_common_subsequence_recurse(X,
                                                              Y,
                                                              m - 1,
                                                              n - 1,
                                                              dp,
                                                              dp_string)
            dp_string.append(X[m - 1])
        return 1 + dp[m-1][n-1]
    else:
        if dp[m][n-1] == -1:
            dp[m][n-1] = longest_common_subsequence_recurse(X,
                                                            Y,
                                                            m,
                                                            n - 1,
                                                            dp,
                                                            dp_string)
        if dp[m-1][n] == -1:
            dp[m-1][n] = longest_common_subsequence_recurse(X,
                                                            Y,
                                                            m - 1,
                                                            n,
                                                            dp,
                                                            dp_string)
        return max(dp[m][n-1], dp[m-1][n])



def longest_common_subsequence(X, Y, m, n, sub_sequence):
    x = 0
    if m > n:
        x = m
    else:
        x = n

    dp = [[-1 for x in range(x+1)] for y in range(x+1)]
    return longest_common_subsequence_recurse(X, Y, m, n, dp, sub_sequence)

X="ABAC BDAB"
Y="BDCAB A"
sub_sequence = []
print("longest common subsequence length={}".format(longest_common_subsequence(X,
                                                                               Y,
                                                                               len(X),
                                                                               len(Y),
                                                                               sub_sequence)))
print("dp_string={}.".format(sub_sequence))