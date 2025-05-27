class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d= 0
        nd=0
        for i in range(n+1):
            if i%m==0:
                d+=i
            else:
                nd+=i
        return nd-d