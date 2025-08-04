class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=-1
        if needle in haystack:
            x=haystack.index(needle)
        return x
        