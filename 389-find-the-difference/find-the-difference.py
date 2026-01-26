class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        c1=Counter(s)
        c2=Counter(t)
        for i in s:
            if i not in t or c1[i]!=c2[i]:
                return i
        for i in t:
            if i not in s or c1[i]!=c2[i]:
                return i
        