"""
Given two sequences X[1..m] and Y[1..n], find the longest common subsequence between them.
Example:
    X: ABAC BDAB
    Y: BDCAB A
    Longest common subsequence: BCBA

"""

def longest_common_subsequence_non_recurse(X, Y, m, n, dp):
    for index1 in range(m):
        for index2 in range(n):
            if X[index1] == Y[index2]:
                if index1 == 0 or index2 == 0:
                    dp[index1][index2] = 1
                else:
                    dp[index1][index2] = dp[index1-1][index2-1] + 1
            else:
                if index1 == 0 or index2 == 0:
                    dp[index1][index2] = 0
                else:
                    dp[index1][index2] = max(dp[index1-1][index2],
                                             dp[index1][index2-1])
        return dp[m-1][n-1]


def longest_common_subsequence_recurse(X, Y, m, n, dp):
    if m == 0 or n == 0:
        return 0

    if X[m-1] == Y[n-1]:
        if dp[m-1][n-1] == -1:
            dp[m-1][n-1] = longest_common_subsequence_recurse(X,
                                                              Y,
                                                              m - 1,
                                                              n - 1,
                                                              dp)
        return 1 + dp[m-1][n-1]
    else:
        if dp[m][n-1] == -1:
            dp[m][n-1] = longest_common_subsequence_recurse(X,
                                                            Y,
                                                            m,
                                                            n - 1,
                                                            dp)
        if dp[m-1][n] == -1:
            dp[m-1][n] = longest_common_subsequence_recurse(X,
                                                            Y,
                                                            m - 1,
                                                            n,
                                                            dp)
        return max(dp[m][n-1], dp[m-1][n])



def longest_common_subsequence(X, Y, m, n):
    x = 0
    if m > n:
        x = m
    else:
        x = n

    dp = [[-1 for x in range(x+1)] for y in range(x+1)]
    return longest_common_subsequence_recurse(X, Y, m, n, dp)

X="ABAC BDAB"
Y="BDCAB A"
sub_sequence = []
print("longest common subsequence length={}".format(longest_common_subsequence(X,
                                                                               Y,
                                                                               len(X),
                                                                               len(Y))))
x = 0
if len(X) > len(Y):
    x = len(X)
else:
    x = len(Y)

dp = [[0 for x in range(x)] for y in range(x)]
print("Non Recurse: longest common subsequence length={}"
      .format(longest_common_subsequence_non_recurse(
              X,
              Y,
              len(X),
              len(Y),
              dp)))

print("dp={}.".format(dp))