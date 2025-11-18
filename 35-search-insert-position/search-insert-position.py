class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def bst(l,r):
            m=(l+r)//2
            if l>r:
                return l
            if nums[m]==target:
                return m
            elif nums[m]<target:
                return bst(m+1,r)
            else:
                return bst(l,m-1)
        return bst(0,len(nums)-1)