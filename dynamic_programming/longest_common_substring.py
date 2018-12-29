"""
Given two sequences X[1..m] and Y[1..n], find the longest common substring between them.
Example:
    X: DEADBEEF
    Y: EATBEEF
    Two common substrings are EA and BEEF.
    The longest is BEEF with length 4, therefore, return 4.

"""

def longest_common_substring_non_recurse2(X, Y, m, n,dp, output_string):
    result = 0

    for index1 in range(m):
        for index2 in range(n):
            if X[index1]==Y[index2]:
                if index1 == 0 or index2 == 0:
                    dp[index1][index2] = 1
                else:
                    dp[index1][index2] = dp[index1-1][index2-1]+1
                if dp[index1][index2] > result:
                    result = dp[index1][index2]
                    output_string[0] = Y[index1:index1+result]
            else:
                dp[index1][index2]=0
    return result


def longest_common_substring_non_recurse(X, Y, m, n, output_string):
    longest_substring_length = 0
    for index1 in range(m):
        for index2 in range(n):
            if X[index1] == Y[index2]:
                index3=index1
                index4=index2
                while index3 < m and index4 < n:
                    if X[index3] == Y[index4]:
                        index3+=1
                        index4+=1
                    else:
                        break
                if index3 == index1:
                    if longest_substring_length == 0:
                        longest_substring_length = 1
                        output_string[0] = X[index1]
                else:
                    substring_length = index3 - index1
                    if substring_length > longest_substring_length:
                        output_string[0] = X[index1:index3]
                        longest_substring_length = substring_length
    return longest_substring_length

def longest_common_substring_recurse(X, Y, m, n, dp, count):
    if m == 0 or n == 0:
        return count

    if X[m-1] == Y[n-1]:
        dp[m-1][n-1] = longest_common_substring_recurse(X,Y,m-1,n-1,dp,count+1)
        count = dp[m-1][n-1]

    if dp[m][n-1] == -1:
        dp[m][n - 1] = longest_common_substring_recurse(X, Y, m, n - 1, dp, 0)
    if dp[m-1][n] == -1:
        dp[m-1][n] = longest_common_substring_recurse(X, Y, m-1, n, dp, 0)

    return max(count,
                dp[m][n-1],
                dp[m-1][n])



X="DEADBEEFXXR"
Y="EATYYBEEF"
output_string = [""]
x = 0
if len(X) > len(Y):
    x = len(X)
else:
    x = len(Y)

dp = [[-1 for x in range(x + 1)] for y in range(x + 1)]
print("longest common substring length={}".format(longest_common_substring_recurse(X,
                                                                           Y,
                                                                           len(X),
                                                                           len(Y),
                                                                           dp,
                                                                           0)))
#print("dp={}".format(dp))
print("Non Recurse1: longest common substring length={}".format(longest_common_substring_non_recurse(X,
                                                                           Y,
                                                                           len(X),
                                                                           len(Y),
                                                                           output_string)))
print("output_string = {}".format(output_string))

print("Non Recurse2: longest common substring length={}".format(longest_common_substring_non_recurse2(X,
                                                                           Y,
                                                                           len(X),
                                                                           len(Y),
                                                                           dp,
                                                                           output_string)))
print("output_string = {}".format(output_string))