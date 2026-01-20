class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        import math
        if len(piles)==h:
            return r
        if len(piles)==1:
            return math.ceil(piles[0]/h)
        l=1
        def bs(l,r):
            m=(l+r)//2
            c=0
            if l==r:
                return l
            for i in piles:
                c+=math.ceil(i/m)
                #print(l,r,m,c,i)
            if c>h:
                return bs(m+1,r)
            
            if c<=h:
                return bs(l,m)
        
        return bs(l,r)
