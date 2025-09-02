class Solution:
    from math import comb

    def uniquePaths(self,m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)