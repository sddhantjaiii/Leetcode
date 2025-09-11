class Solution:
    def hIndex(self, citations: List[int]) -> int:
        a=sorted(citations,reverse=True)
        n=len(a)
        for i in range(n):
            if a[i]<i+1:
                return i
        return n