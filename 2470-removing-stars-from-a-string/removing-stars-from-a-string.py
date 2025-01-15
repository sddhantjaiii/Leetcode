class Solution:
    def removeStars(self, s: str) -> str:
        x=""
        for j in s:
            if j=="*":
                x=x[:-1]
            else:
                x+=j
        return x
        