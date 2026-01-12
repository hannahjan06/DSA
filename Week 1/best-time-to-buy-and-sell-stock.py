"""
runtime: 133ms
time complexity: O(n)
space complexity: O(n)
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
tags: #array #dynamic-programming
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit