class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        l=len(nums)
        r=[]
        n=l/3
        s=set(nums)
        for i in s:
            x=i
            if c[x]>n:
                r.append(x)
        return r

        