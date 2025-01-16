class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        u=len(nums)
        p=[]
        s=[1]*len(nums)
        f=1
        r=[1]*u
        for i in nums:
            p.append(f)
            f*=i
        f=1
        for j in range(u - 1, -1, -1):
            s[j] = f
            r[j] = p[j] * s[j]
            f *= nums[j]
        
        return r