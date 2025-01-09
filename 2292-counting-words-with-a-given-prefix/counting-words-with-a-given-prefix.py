class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in words:
            k=0
            for j in pref:
                if len(pref)<=len(i):
                    if i[k]==j:
                        
                        k+=1
            print(c,k,len(pref))
            if k==len(pref):
                c+=1
                print(i,j,c)
        return c
            