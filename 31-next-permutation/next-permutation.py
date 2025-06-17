class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l==1:
            return nums
        for i in range(l-1,0,-1):
            if nums[i]>nums[i-1]:
                break
        m1=float("inf")
        x=-1
        for j in range(l-1,i-1,-1):
            m=nums[j]
            if m1>m and m>nums[i-1]:
                m1=m
                x=j
        nums[i-1],nums[x]=nums[x],nums[i-1]
        nums[:]=nums[:i]+nums[l-1:i-1:-1]
        if x==-1:
            return nums.sort()
    

        