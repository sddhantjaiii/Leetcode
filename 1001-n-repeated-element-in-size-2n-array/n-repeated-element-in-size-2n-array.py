class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        c=1
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==prev :
                c+=1
            else:
                prev=nums[i]
                c=1
            if c==len(nums)//2:
                return nums[i]