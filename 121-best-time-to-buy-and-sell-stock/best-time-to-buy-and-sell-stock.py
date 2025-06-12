class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        p=0
        for i in range(1,len(prices)):
            cost=prices[i]-m
            p=max(p,cost)
            m=min(m,prices[i])
        return p