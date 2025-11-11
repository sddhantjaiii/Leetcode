class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        #4 5 6 7 0
        while left<right:
            mid=(left+right)//2
            
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
            print(left,mid,right)
        return nums[left]
            
