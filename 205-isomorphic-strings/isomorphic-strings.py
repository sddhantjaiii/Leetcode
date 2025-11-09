class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import Counter
        sc=Counter(s)
        tc=Counter(t)
        s1=[]
        t1=[]
        for key,value in sc.items():
            s1.append(value)
        for key,value in tc.items():
            t1.append(value)
        s1.sort()
        t1.sort()
        x={}
        if s1==t1:
            for i in range(len(s)):
                if s[i] in x:
                    if x[s[i]]==t[i]:
                        continue
                    else:
                        return False
                else:
                    x[s[i]]=t[i]
            return True
        else:
            return False
                     
            
        