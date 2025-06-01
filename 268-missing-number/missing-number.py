class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for i in range(max(nums)+5):
            if i not in nums:
                return i
