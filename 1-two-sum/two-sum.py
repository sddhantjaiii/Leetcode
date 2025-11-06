class Solution:
    def twoSum(self, nums, target):
        d={}
        for i,j in enumerate(nums):
            if target-j in d:
                return d[target-j],i
            d[j]=i