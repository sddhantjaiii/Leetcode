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
            t=nums[j]
            nums[j] = f
            f *= t
        for i in range(u):
            nums[i]=p[i]*nums[i]
        print(p,s)
        return nums