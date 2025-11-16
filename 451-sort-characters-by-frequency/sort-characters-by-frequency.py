"""class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c=Counter(s)
        m=max(c.values())
        r=""
        f=[[] for __ in range(m+1)]
        for key,value in c.items():
            f[value].append(key)
        for i in range(len(f)-1,-1,-1):
            if f[i] != []:
                for j in f[i]:
                    r+=j*c[j]

        return r"""
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = Counter(s)
        items = list(c.items())
        items.sort(key=lambda item:item[1], reverse=True)
        result=""
        for character, frequency in items:
            result+=(character * frequency)
        return result
