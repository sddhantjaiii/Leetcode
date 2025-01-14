class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d=[]
        x=0
        for i in range(len(A)):
            p1=A[:i+1]
            p2=B[:i+1]
            p1=set(p1)
            p2=set(p2)
            for j in p1:
                if j in p2:
                    x+=1
            d.append(x)
            x=0
        return d
            

            
        