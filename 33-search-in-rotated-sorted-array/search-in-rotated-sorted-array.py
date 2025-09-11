class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m=nums[0]
        
        def binarysearch(left,right,m):
            mid=(left+right)//2
            
            if left==right:
                return 0
            if nums[mid]>nums[mid+1]:
                return mid +1
            if nums[mid]<nums[mid+1] and nums[mid]>m:
                m=max(nums[mid+1],m)
                return binarysearch(mid+1,right,m)
            else:
                m=max(nums[mid+1],m)
                return binarysearch(left,mid,m)

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1


        f=binarysearch(0,len(nums)-1,m)
        newarr=nums[f:]+nums[:f]
        x=len(nums)**(0.5)
        def bs(left,right):
            
            mid=(left+right)//2
            print(left,right,newarr)
            
            if target==newarr[mid]:
                return mid
            if left==right:
                return -1
            if newarr[mid]>target:
                return bs(left,mid)
            else:
                return bs(mid+1,right)
            
        meow=bs(0,len(nums)-1)
        if meow==-1:
            return -1
        y=(meow+f+len(nums))%len(nums)
        
        return abs(y)
