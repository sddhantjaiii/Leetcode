class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d=[]
        x=0
        for i in range(len(A)):
            p1=set(A[:i+1])
            p2=set(B[:i+1])
            for j in p1:
                if j in p2:
                    x+=1
            d.append(x)
            x=0
        return d
            

            
        