class Solution:
    def removeStars(self, s: str) -> str:
        x=[]
        for i,j in enumerate(s):
            if j=="*":
                x.pop()
            else:
                x.append(j)
        return "".join(x)
        