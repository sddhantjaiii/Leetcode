class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        l=len(baskets)
        m=max(baskets)
        for i in fruits:
            if i>m:
                continue
            for j in range(l):
                if i<=baskets[j]:
                    baskets[j]=0
                    c+=1
                    break
        return l-c
                
            


