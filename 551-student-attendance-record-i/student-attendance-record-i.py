class Solution:
    def checkRecord(self, s: str) -> bool:
        from collections import Counter
        c=Counter(s)
        if c['A']<2:
            if "LLL" in s:
                return False
            else:
                return True
        return False