class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        k=0
        for i in s:
            nums[k]=i
            k+=1
        return len(s)
        