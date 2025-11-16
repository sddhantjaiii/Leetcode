class Solution:
    def maxDepth(self, s: str) -> int:
        from collections import deque
        m=0
        r=0
        for i in s:
            if i == "(":
                r+=1
                m=max(m,r)
            elif i== ")":
                r-=1
        return m
            
        