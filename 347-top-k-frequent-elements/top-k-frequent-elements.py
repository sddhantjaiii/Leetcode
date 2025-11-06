class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        x=[]
        for key,value in c.items():
            x.append([value,key])
        x.sort(reverse=True)
        r=[]
        for i in range(k):
            r.append(x[i][1])
        return r


