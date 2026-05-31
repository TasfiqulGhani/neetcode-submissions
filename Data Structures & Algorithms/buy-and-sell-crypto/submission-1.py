class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]
        for sell in prices:
            profit = sell - buy

            if profit > 0:
                result = max(result,  profit)
            else:
                buy = sell
        return result
        