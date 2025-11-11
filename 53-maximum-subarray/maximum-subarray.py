class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        y=max(nums)
        if y<0:
            return y
        m=0
        k=0
        for i in nums:
            k+=i
            m=max(m,k)
            if k<0:
                k=0
        return m
        