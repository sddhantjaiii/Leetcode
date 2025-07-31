class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        l=len(nums)
        r=[]
        n=l/3
        for i in c:
            if c[i]>n:
                r.append(i)
        return r

        