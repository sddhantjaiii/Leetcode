class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0

        l=len(derived)
        o=[0]*l
        o1=[0]*l
        for i in range(l-1):
            o[i+1]=o[i]^derived[i]
        
        o1[l-1]=1^derived[l-1]
        x,x1=[0]*l,[0]*l
        for i in range(l):
            if i==l-1:
                x[i]=o[0]^o[i]
                x1[i]=o1[0]^o1[i]
            else:
                x[i]=o[i]^o[i+1]
                x1[i]=o1[i]^o1[i+1]
        if x==derived or x1==derived:
            return True
        return False
        