class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<1:
            return 0
        if len(s)<2:
            return 1
        if len(s)<3:
            return 2
        
        l=len(s)
        c=Counter(s)
        x=0
        for key, value in c.items():
            while(value>=3):
                value-=2
            x+=value
        return x




        