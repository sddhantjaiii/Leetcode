class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c=Counter(s)
        r=""
        f=[[] for __ in range(100000)]
        for key,value in c.items():
            f[value].append(key)
        for i in range(len(f)-1,-1,-1):
            if f[i] != []:
                for j in f[i]:
                    r+=j*c[j]

        return r
