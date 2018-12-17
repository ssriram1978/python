"""
Say you have an array for which the ith element is the price of a given
stock on day i.
If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find
the maximum profit.
Examples:
    input [7,1,5,3,6]
    output 5
    max difference = 6-1=5 not 7-1=6 as selling price needs to be larger
    than buying price.

"""
def max_profit(array):
    profit = 0
    end = len(array)
    min = array[0]
    for index in range(len(array)):
        if array[index] < min:
            min = array[index]

        if index + 1 < end and array[index+1] > array[index]:
            profit = max(profit, array[index+1]-min)

    return profit


array = [7,1,5,3,6,4,8,9,0,11,1,15]
print("max profit = {}".format(max_profit(array)))


"""
Cutting Rods:
Given a rod of length n and prices P[i] for i = 1, ..., n, where P[i] is the
price of a rod of length i. Find the maximum total revenue you can
make by cutting and selling the rod (Assume no cost for cutting rod).
"""
def max_revenue(list_of_costs):
    pass

list_of_costs=[1,5,8,9,10]
print("max revenue = {}".format(max_revenue(list_of_costs)))


"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only
constraint stopping you from robbing each of them is that adjacent
houses have security system connected and it will automatically
attract the police if two adjacent houses were broken into on the 
same night.
"""
def max_robbery(house_values):

house_values=[1,10,9,6,14,3,8]
print("max robbery = {}".format(max_revenue(house_values)))


"""
Climbing stairs:
You can climb one or two stairs with one step. How many different ways can
you climb n stairs?
"""
