class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        l=len(nums)
        while i < l:
            if nums[i]==0:
                nums[:]=nums[:i]+nums[i+1:]+nums[i:i+1]
                l-=1
                continue
            i+=1
            