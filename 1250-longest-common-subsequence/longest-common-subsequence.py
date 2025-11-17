class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1=len(text1)
        l2=len(text2)
        dp=[[-1 for __ in range(l2)] for _ in range(l1)]
        print(dp)
        def pmc(ix1,ix2):
            if ix1<0 or ix2<0:
                return 0
            if dp[ix1][ix2]!=-1:
                return dp[ix1][ix2]
            if text1[ix1]== text2[ix2]:
                dp[ix1][ix2]=1+pmc(ix1-1,ix2-1)
            else:
                dp[ix1][ix2]=0+max(pmc(ix1-1,ix2),pmc(ix1,ix2-1))
            return dp[ix1][ix2]
        r=pmc(l1-1,l2-1)
        return r

        