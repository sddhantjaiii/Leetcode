class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<=nums[0]:
            return 0
        def bst(l,r):
            m=(l+r)//2
            if l>=r:
                return l+1
            if nums[m]<target<=nums[m+1]:
                return m+1
            elif nums[m]<target:
                return bst(m+1,r)
            else:
                return bst(l,m-1)
        return bst(0,len(nums)-1)