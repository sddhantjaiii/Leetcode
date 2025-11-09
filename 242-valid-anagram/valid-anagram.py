class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sc=Counter(s)
        tc=Counter(t)
        l=len(s)
        l1=len(t)
        if l1!=l:
            return False
        for key,value in sc.items():
            if tc[key]==value:
                continue
            else:
                return False
        return True