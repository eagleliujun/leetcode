"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


def maxProfit(prices):
    lens = len(prices)
    profit = [[0 for _ in range(2)] for _ in range(lens)]
    # profit[lens][1 or 0]: lens:days  1 : hold stock  0: hold money
    for i in range(lens):
        if i == 0:
            profit[0][0] = 0
            profit[0][1] = -prices[0]
        else:
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i])
            profit[i][1] = max(profit[i - 1][1], -prices[i])
    return profit[lens - 1][0]

def maxProfit2(prices):
    lens = len(prices)
    profit0, profit1 = 0, -prices[0]
    for i in range(1,lens):
        profit0 = max(profit0, profit1 + prices[i])
        profit1 = max(profit1, -prices[i])
    return profit0


def maxProfit3(prices):
    lens = len(prices)
    profit0, profit1 = 0, -prices[0]
    for i in range(1,lens):
        profit0 = profit1 + prices[i] if profit1 + prices[i] > profit0 else profit0
        profit1 = -prices[i] if profit1 + prices[i] > 0 else profit1
    return profit0

p1 = [7, 1, 5, 3, 6, 4]
p2 = [7, 6, 4, 3, 1]
print(maxProfit2(p1))
