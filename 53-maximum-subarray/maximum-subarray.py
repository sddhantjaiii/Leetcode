class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        m=float("-inf")
        for i in nums:
            sum+=i
            m=max(m,sum)
           
            if sum<=0:
                sum=0
        return m