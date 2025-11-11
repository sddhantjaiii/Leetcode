class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c=Counter(nums)
        for key,value in c.items():
            if value >1:
                return True
        return False