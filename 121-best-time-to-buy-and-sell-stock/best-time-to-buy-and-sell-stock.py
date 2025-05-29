class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price<min_price:
                min_price = price
            profit = price - min_price
            max_profit = max(max_profit,profit)
        return max_profit
        # sliding minimum approach or single pass approach
        # TC:O(N),SC:O(1)