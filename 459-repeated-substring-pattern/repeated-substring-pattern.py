class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=s+s
        s2=s1[1:-1]
        return s in s2
