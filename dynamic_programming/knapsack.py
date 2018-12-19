"""
A set of n items, where item i has weight w[i] and value V[i], and a
knapsack with capacity W.
Suppose to pick a "few" items from the n elements such that their
weight is less than or equal to W but their summed value is maximized.

Example:
    W=8, n=3
    w[1]=2, V[1]=10
    w[2]=5, V[2]=12
    w[3]=8, V[3]=21
    Optimum is choose 1 of object1 and 1 of object 2 for a total weight of 2+5=7
    and total value of 10+12 = 22. This is the maximum possible value with weight = 8.
    input=[array of [weight1,value1],[weight2,value2],...]
    input = [[5,10],[4,40],[6,30],[3,50]]

"""

def max_value_of_knapsack_recurse(max_weight,
                                  list_of_weights,
                                  list_of_priorities,
                                  current_index):

    if current_index <= 0:
        return 0
    if list_of_weights[current_index - 1] > max_weight:
        return max_value_of_knapsack_recurse(max_weight,
                                             list_of_weights,
                                             list_of_priorities,
                                             current_index - 1)
    else:
        return max(list_of_priorities[current_index-1] +
                   max_value_of_knapsack_recurse(max_weight-list_of_weights[current_index-1],
                                                 list_of_weights,
                                                 list_of_priorities,
                                                 current_index - 1),
                   max_value_of_knapsack_recurse(max_weight,
                                                 list_of_weights,
                                                 list_of_priorities,
                                                 current_index - 1)
                   )


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack_non_recurse(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

list_of_priorities = [60, 100, 120, 10]
list_of_weights = [10, 20, 30, 40]
max_weight = 50
print("For max weight {}, max_value_of_knapsack={}".format(max_weight,
max_value_of_knapsack_recurse(max_weight,
                              list_of_weights,
                              list_of_priorities,
                              len(list_of_weights))))
max_weight = 8
list_of_priorities = [10, 12, 21]
list_of_weights = [2, 5, 8]

print("For max weight {}, max_value_of_knapsack={}".format(max_weight,
max_value_of_knapsack_recurse(max_weight,
                              list_of_weights,
                              list_of_priorities,
                              len(list_of_weights))))


print("Non recurse: For max weight {}, max_value_of_knapsack={}".format(max_weight,
knapSack_non_recurse(max_weight,
                              list_of_weights,
                              list_of_priorities,
                              len(list_of_weights))))

