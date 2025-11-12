class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1=0
        x2=0
        for i in range(len(nums)):
            x1=x1^(i+1)
            x2=x2^(nums[i])
        return x1^x2