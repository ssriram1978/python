"""
Given a rod of length n and prices P[i] for i = 1,2,...n
where P[i] is the price of the rod of length i.
Find the maximum total revenue you can make by cutting and
selling the rod (Assume no cost for cutting the rod).


max_revenue = max(P[1]+R[n-1],P[2]+R[n-2],P[3]+R[n-3],P[4]+R[n-4],....,P[n-1]R[1],P[n]

Base case: if n <=0:
               return 0
           elif n == 1:
               return P[1]
           else:

"""


def find_max_revenue_recurse(rod_length,
                             price_of_rod_per_length,
                             cache):
    max_revenue = 0
    if rod_length == 0:
        return 0
    elif rod_length == 1:
        return price_of_rod_per_length[0]
    else:
        for index in range(rod_length-1,-1,-1):
            if not cache[rod_length-index-1]:
                cache[rod_length - index - 1] = find_max_revenue_recurse(rod_length-index-1,
                                                                         price_of_rod_per_length,
                                                                         cache)
            max_revenue=max(max_revenue,
                            price_of_rod_per_length[index]+cache[rod_length - index - 1])
    return max_revenue


def find_max_revenue(rod_length, price_of_rod_per_length):
    cache = [0] * len(price_of_rod_per_length)
    return find_max_revenue_recurse(rod_length,
                                    price_of_rod_per_length,
                                    cache)

def find_max_revenue_non_recurse(rod_length,
                                 price_of_rod_per_length):
    dp = [0] * rod_length
    for index in range(rod_length):
        if index == 0:
            dp[index] = price_of_rod_per_length[index]
        elif index == 1:
            dp[index] = max(price_of_rod_per_length[index],
                            price_of_rod_per_length[index-1]*2)
        else:
            dp[index] = price_of_rod_per_length[index]
            for index2 in range(index-1,-1,-1):
                dp[index] = max(dp[index], price_of_rod_per_length[index2] + dp[index-index2-1])
    return dp[rod_length-1]

price_of_rod_per_length = [1,3,2,1,2,1,5]
for index in range(len(price_of_rod_per_length)):
    print("Recurse: maximum profit that you can get by cutting rod of length {} is {}."
          .format(index+1, find_max_revenue(index+1, price_of_rod_per_length)))
    print("Non-Recurse: maximum profit that you can get by cutting rod of length {} is {}."
          .format(index+1, find_max_revenue_non_recurse(index+1, price_of_rod_per_length)))
