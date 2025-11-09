class Solution:
    def reverseWords(self, s: str) -> str:
        l=len(s)
        r=""
        t=""
        for i in range(l-1,-1,-1):
            if s[i]==" ":
                if t== "":
                    t=""
                    continue
                r=r+t[::-1]+" "
                t=""
            else:
                t+=s[i]
                
        r+=t[::-1]
        return r.strip()
