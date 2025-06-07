class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        l=len(nums)-1
        for i in range(l+1):
            
            if nums[i]==val:
                continue
            nums[c]=nums[i]
            c+=1
        return c