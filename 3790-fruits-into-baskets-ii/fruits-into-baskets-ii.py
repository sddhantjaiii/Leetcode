class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        r=[0 for __ in range(len(baskets))]
        for i in fruits:
            for j in range(len(baskets)):
                if i<=baskets[j] and r[j]==0:
                    r[j]=1
                    c+=1
                    break
        print(r)
        return len(baskets)-c
                
            


