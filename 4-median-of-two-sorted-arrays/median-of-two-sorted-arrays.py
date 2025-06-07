class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c=nums1+nums2
        c.sort()
        l=len(c)
        if l%2==0:
            m=int(l/2)-1
            
            return float(c[m]+c[m+1])/2
        m=int(l/2)
        return float(c[m])