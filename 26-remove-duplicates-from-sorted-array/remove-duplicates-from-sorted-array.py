class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        s=sorted(s)
        l=len(s)
        k=0
        for i in s:
            nums[k]=i
            k+=1
        return l
        