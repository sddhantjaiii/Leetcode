class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in words:
            k=0
            for j in pref:
                if len(pref)<=len(i):
                    if i[k]==j:  
                        k+=1
            if k==len(pref):
                c+=1
        return c
            