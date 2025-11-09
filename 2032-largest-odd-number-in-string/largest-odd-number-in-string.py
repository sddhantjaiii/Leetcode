class Solution:
    def largestOddNumber(self, num: str) -> str:
        r=""
        l=len(num)
        
        for i in range(l-1,-1,-1):
            x=int(num[i])
            if (x)%2==1:
                return num[:i+1]
                

        return ""