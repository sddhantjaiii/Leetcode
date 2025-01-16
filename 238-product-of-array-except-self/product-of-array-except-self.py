class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        u=len(nums)
        p=[]
        s=[1]*len(nums)
        f=1
        for i in nums:
            p.append(f)
            f*=i
            
        
        f=1
        for j in range(u - 1, -1, -1):
            s[j] = f
            f *= nums[j]
        
        for i in range(u):
            nums[i]=p[i]*s[i]
        return nums