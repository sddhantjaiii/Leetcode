class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x=0
        f=0
        if n<=0:
            return False
        while f<=n:
            if 3**x==n:
                return True
            x+=1
            f=3**x 
        return False
        