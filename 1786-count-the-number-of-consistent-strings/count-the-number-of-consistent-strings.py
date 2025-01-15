class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        allowed=set(allowed)
        for i in words:  
            for j in i:
                if j not in allowed:
                    break
            else:
                c+=1 
        return c