class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        print(l)
        x=nums[l:]+nums[:l]
        print(x)
        nums=x
        y=l
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return (mid+y)%(len(nums))
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        
        return -1




            