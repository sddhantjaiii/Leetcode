from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        c=Counter(nums)
        m=max(c,key=c.get)
        if l/2<c[m]:
            return m


        