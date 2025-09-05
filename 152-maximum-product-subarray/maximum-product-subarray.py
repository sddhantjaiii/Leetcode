class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nums[0]
        temp=1
        temp1=1
        l=len(nums)
        for i in range(l):
            j=l-i-1
            if temp==0:
                temp=1
            if temp1==0:
                temp1=1
            temp*=nums[i]
            temp1*=nums[j]
            a=max(a,temp1,temp)
        return a