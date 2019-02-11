
"""
Write a function that computes the minimum number of coins needed to match the desired input value.
Example: n = 16, coins = [1,5,10,25]
You could use one 1 cent coin + one 5 cent coin + one 10 cent coin to match n=16.
Return the output as 3.
dp[rows=coins][columns= 0 to n]
    0  1  2  3  4  5  6  7  8  9  10 11  12   13   14  15  16
1   0  1  2  3  4  5  6  7  8  9  10 11  12   13   14  15  16
5   0  1  2  3  4  1  2  3  4  5   2  3   4    5    6   3   4
10  0  1  2  3  4  1  2  3  4  5   1  2   3    4    5   2   3
25  0  1  2  3  4  1  2  3  4  5   1  2   3    4    5   2   3

return dp[-1][-1]
"""

def min_num_of_coins(n,list_of_coins):
    dp = [[0 for _ in range(n+1)]  for _ in range(len(list_of_coins))]
    current_row=0
    current_column = 0
    for current_row in range(0,len(list_of_coins)):
        for current_column in range(1,n+1):
            quotient = current_column//list_of_coins[current_row]
            reminder = current_column%list_of_coins[current_row]
            if not quotient:
                #current coin is greater than the current total.
                if not current_row:
                    #first row, mark it as 0.
                    dp[current_row][current_column] = 0
                else:
                    #copy whatever was computed in the previous row.
                    dp[current_row][current_column] = dp[current_row-1][current_column]
            else:
                #the current coin can divide the current total.
                if not reminder:
                    #no reminder. no more to search. 
                    dp[current_row][current_column] = quotient
                else:
                    #walk back and find all the coins that can sum up to the reminder.
                    dp[current_row][current_column] = quotient
                    walk_back_rows = current_row-1
                    while walk_back_rows >=0:
                        quotient = reminder//list_of_coins[walk_back_rows]
                        reminder = reminder%list_of_coins[walk_back_rows]
                        if quotient:
                            dp[current_row][current_column] += quotient
                            if not reminder:
                                break
                        walk_back_rows-=1            
                    if reminder:
                        print("After computing the total number of coins to be {} to match {}, there is still a reminder of {}."
                        .format(dp[current_row][current_column],current_column,reminder))
                        dp[current_row][current_column] = -1
    return dp[-1][-1]

def min_num_of_coins2(n,list_of_coins):
    dp = [0 for _ in range(n+1)]
    for coin in list_of_coins:
        #mark these coins as 1 in the dp list.
        if coin <= n:
            dp[coin]=1
    for current_min_num_of_coins in range(1,n+1):
        dp[current_min_num_of_coins] = min(1+dp[current_min_num_of_coins-list_of_coins[index]] \
        for index in range(len(list_of_coins)) if current_min_num_of_coins - list_of_coins[index] >= 0 )
    return dp[-1]

list_of_coins = [1,5,10,25]
for index in range(1,26):
    print("minimum number of coins needed to make n={} is {}.".format(index,min_num_of_coins(index,list_of_coins)))
    print("minimum number of coins needed to make n={} is {}.".format(index,min_num_of_coins2(index,list_of_coins)))