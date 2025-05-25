class Solution:
    def minimumSteps(self, s: str) -> int:
        b=0
        for i in range(len(s)-1,0,-1):
            if s[i]=="0":
                b=i
                break
        c=0
        for i in range(len(s)-1,-1,-1):
            if i>b:
                continue
            if s[i]=="1":
                c+=b-i
                b-=1
        return c
            