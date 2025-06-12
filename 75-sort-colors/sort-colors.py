from collections import Counter
class Solution:
    def sortColors(self, nums):
        c=Counter(nums)
        nums[:]=[0]*c[0]+[1]*c[1]+[2]*c[2]
        