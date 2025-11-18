class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        print(s)
        r=""
        l=len(s)
        t=""
        r="  "+r
        
        for i in range(l-1,-1,-1):
            if s[i]==" ":
                r=r.strip()
                t=t.strip()
                r+=" "+t
                t=""
            t=s[i]+t
        t=t.strip()
        r=r.strip()
        r=r+" "+t
        return r.strip()