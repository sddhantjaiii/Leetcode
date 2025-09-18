class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=sum(nums)
        y=set(nums)
        l=len(nums)
        l1=len(y)
        dif=l-l1
        z=sum(y)
        return (x-z)//dif