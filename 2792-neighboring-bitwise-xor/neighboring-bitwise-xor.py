class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        l=len(derived)
        o=[0]*l
        for i in range(l-1):
            o[i+1]=o[i]^derived[i]
        o1=[1]*l
        for i in range(l-1):
            o1[i+1]=o1[i]^derived[i]
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
        