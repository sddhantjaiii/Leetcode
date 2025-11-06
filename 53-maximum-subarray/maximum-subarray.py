class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        y=max(nums)
        if y<0:
            return y
        m=0
        k=0
        for i in nums:
            x=k+i
            if x<0:
                k=0
            else:
                k+=i
            m=max(k,m)
        return m
        