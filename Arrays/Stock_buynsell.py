class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        max_profit = 0
        buy = prices[0]
        sell = 0
        for idx,n in enumerate(prices):
            sell = n
            curr_profit = sell-buy
            if curr_profit > max_profit:
                max_profit  = curr_profit
            if curr_profit<=0:
                buy = n
        return max_profit