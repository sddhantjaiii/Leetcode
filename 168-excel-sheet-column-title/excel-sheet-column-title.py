class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c=columnNumber
        r=""
        d = {i: chr(64 + i) for i in range(1, 27)}

        while c > 0:
            c -= 1  
            r = d[(c % 26) + 1] + r
            c //= 26
            print(c)
        return r
            
        