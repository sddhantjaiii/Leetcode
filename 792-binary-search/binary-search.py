class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(l,r):
            m=(l+r)//2
            if l>r:
                return -1
            if nums[m]==target:
                print(m)
                return m
            elif nums[m]<target:
                return bst(m+1,r)
            else:
                return bst(l,m-1)
        
        return bst(0,len(nums)-1)
        
        