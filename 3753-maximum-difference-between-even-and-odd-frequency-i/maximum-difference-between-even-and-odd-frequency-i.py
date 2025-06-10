from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        odd=0
        even=float('inf')
        for v,key in c.items():
            print(key)
            if key%2 !=0:
                odd=max(odd,key)
            else:
                even=min(even,key)
        return odd-even