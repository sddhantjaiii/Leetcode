class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        k=len(s)-1
        if (k+1) % 2 != 0:
            return False
        o=0
        a=0
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
        i=k
        o=0
        a=0
        while(i>0):
            if locked[i]=="1":
                if s[i]==")":
                    o+=1
                else:
                    o-=1
            else:
                a+=1
            if a+o<0:
                return False
            i-=1
        return True
            