class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=prod(nums)
        r=[]
        for j,i in enumerate(nums):
            if i==0:
                
                f=prod(nums[:j]+nums[j+1:])
                r.append(f)
                continue
            r.append(m//i)
        return r