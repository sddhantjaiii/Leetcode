class Solution:
    def removeStars(self, s: str) -> str:
        x=[]
        for j in s:
            if j=="*":
                x.pop()
            else:
                x.append(j)
        return "".join(x)
        