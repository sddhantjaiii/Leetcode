class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        b=0
        u=0
        for i in range(len(s)):
            if s[i]=="(":
                b+=1
            else:
                if b>0:
                    b-=1
                else:
                    u+=1
        f=b+u
        
        return f