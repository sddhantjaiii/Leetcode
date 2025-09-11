class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m=nums[0]
        xx=len(nums)**0.5
        def binarysearch(left,right,m,xx):
            mid=(left+right)//2
            xx-=1
            if left==right:
                return -1
            if nums[mid]>nums[mid+1]:
                return mid 
            if nums[mid]<nums[mid+1] and nums[mid]>m:
                m=max(nums[mid+1],m)
                return binarysearch(mid+1,right,m,xx)
            else:
                m=max(nums[mid+1],m)
                return binarysearch(left,mid,m,xx)

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        x=abs(nums[0]-nums[1])
        f=binarysearch(0,len(nums)-1,m,xx)
        newarr=nums[f+1:]+nums[:f+1]
        x=len(nums)**(0.5)
        def bs(x,left,right):
            x-=1
            mid=(left+right)//2
            if x<=-5:
                return -1
            if target==newarr[mid]:
                return mid
            if newarr[mid]>target:
                return bs(x,left,mid)
            else:
                return bs(x,mid+1,right)
        meow=bs(x,0,len(nums)-1)
        if meow==-1:
            return -1
        y=(meow+f+1+len(nums))%len(nums)
        
        return abs(y)
