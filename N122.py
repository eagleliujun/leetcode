"""

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


def maxProfit1(prices):
    lens = len(prices)
    profit = [[0 for _ in range(2)] for _ in range(lens)]
    # profit[lens][1 or 0]: lens:days  1 : hold stock  0: hold money
    for i in range(lens):
        if i == 0:
            profit[0][0] = 0
            profit[0][1] = -prices[0]
        else:
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i])
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
    return profit[lens - 1][0]


def maxProfit2(prices):
    lens = len(prices)
    profit0 = 0
    profit1 = -prices[0]
    for i in range(1,lens):
        profit0 = max(profit0, profit1 + prices[i])
        profit1 = max(profit1, profit0 - prices[i])
    return profit0


p1 = [7, 1, 5, 3, 6, 4]
p2 = [1, 2, 3, 4, 5]
p3 = [7, 6, 4, 3, 1]
print(maxProfit1(p1))
