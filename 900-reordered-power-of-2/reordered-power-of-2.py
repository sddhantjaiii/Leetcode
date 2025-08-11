from itertools import permutations 
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        l=len(str(n))
        for perm in permutations (str(n),l):
            if perm[0]=='0':
                continue
            r="".join(perm)
            b=bin(int(r))
            b=str(b)
            x="0"+b[3:]
            if int(x,2)==0:
                return True
        return False



        