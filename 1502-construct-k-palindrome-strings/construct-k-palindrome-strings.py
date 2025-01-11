class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        c = Counter(s)
        oc = 0
        for char, count in c.items():
            if count % 2 == 1:  
                oc += 1
        return oc <= k
