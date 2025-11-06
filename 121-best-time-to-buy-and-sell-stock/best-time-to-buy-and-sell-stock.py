class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        profit=0
        for i,j in enumerate(prices):
            m=min(j,m)
            profit=max(profit,j-m)
        return profit