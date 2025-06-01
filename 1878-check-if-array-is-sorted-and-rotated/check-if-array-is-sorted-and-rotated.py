class Solution:
    def check(self, nums: List[int]) -> bool:
        l=len(nums)
        u=nums
        x=[0]
        for i in range(l-1):
            if nums[i]<=nums[i+1]:
                continue
            x=nums[i+1:] + nums[:i+1]
            break
        nums.sort()
        print(x)
        if nums==x or x[0]==0 :
            if x[0]==0:
                
                if u==nums:
                    return True
            return True
        return False
