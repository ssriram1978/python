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

X="ABAC BDAB"
Y="BDCAB A"
print("longest common subsequence length={}".format(lcs(X,Y,len(X),len(Y))))