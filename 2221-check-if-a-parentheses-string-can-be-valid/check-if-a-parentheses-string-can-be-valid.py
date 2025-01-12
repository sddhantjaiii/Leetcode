class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        k=len(s)-1
        if (k+1) % 2 != 0:
            return False
        o=0
        a=0
        o1=0
        a1=0

        for i in range(k+1):
            if locked[i]=="1":
                if s[i]=="(":
                    o+=1
                else:
                    o-=1
            else:
                a+=1
            if a+o<0:
                return False
            if locked[k]=="1":
                if s[k]==")":
                    o1+=1
                else:
                    o1-=1
            else:
                a1+=1
            if a1+o1<0:
                return False
            k-=1
        return True
            