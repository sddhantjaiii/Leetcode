class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        q=0
        for i in words:
            allowed=set(allowed)
            i=set(i)
            for j in i:
                if j in allowed:
                    c+=1
                else:
                    break
            
            
            if c==len(i):
                q+=1
            c=0
        return q