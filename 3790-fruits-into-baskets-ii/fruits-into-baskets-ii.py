class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        l=len(baskets)
        r=[0 for __ in range(l)]
        for i in fruits:
            for j in range(l):
                if i<=baskets[j] and r[j]==0:
                    baskets[j]=0
                    c+=1
                    break
        return l-c
                
            


