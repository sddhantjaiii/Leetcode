class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        c=0
        """for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=-1
        x=[]
        for i in range(len(nums)):
            if nums[i]!=-1:
                x.append(nums[i])
        nums=x"""
        prev=nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if  prev>nums[i]<nums[i+1] or prev<nums[i]>nums[i+1]:
                c+=1 
            prev=nums[i]
            print(nums[i],prev,c)
        return c
            
