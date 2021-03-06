"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
"""
Algo1: (buy only only when stocks plunge (huge dip), sell as soon as you see a chance of making profit)
--------------------------------------------------------------------------------------------------------
1. Find and store the index which has an element lesser than the previous element. (buy)
2. Starting from the index found at step1, find and store the index which has an element greater than previous index.(sell)
3. Compute the difference between the elements found at the indexes.
4. Skip the next index.
5. Repeat step 1 to 4 until you reach the end of the loop.

Algo2: (buy only only when stocks plunge (huge dip), sell only when the stock price is going to dip the next day.)
------------------------------------------------------------------------------------------------------------------
1. Find and store the index which has an element lesser than the previous element. (buy)
2. Starting from the index found at step1, find and store the index which has current element greater than next index.(sell)
3. Compute the difference between the elements found at the indexes.
4. Skip the next index.
5. Repeat step 1 to 4 until you reach the end of the loop.

Algo3: (buy immediately and wait for max profit and then sell it.)
------------------------------------------------------------------
1. Find and store the index which has an element lesser than the next element.(buy)
2. Starting from the index found at step1, find and store the index which has current element greater than next index.(sell)
3. Compute the difference between the elements found at the indexes.
4. Skip the next index.
5. Repeat step 1 to 4 until you reach the end of the loop.

Algo4: (buy immediately,sell as soon as you see a chance of making profit.)
---------------------------------------------------------------------------
1. Find and store the index which has an element lesser than the next element.(buy)
2. Starting from the index found at step1, find and store the index which has current element greater than next index.(sell)
3. Compute the difference between the elements found at the indexes.
4. Skip the next index.
5. Repeat step 1 to 4 until you reach the end of the loop.

Return the answer which results in maximum profit among these 4 algo.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
