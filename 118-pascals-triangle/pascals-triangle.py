class Solution(object):
    def generate(self,numRows):
        t = [[] for _ in range(numRows + 1)]
        t[0]=[1]
        t[1]=[1,1]
        for i in range(2,numRows):
            k=len(t[i-1])
            t[i].append(1)
            for j in range(1,k):
                t[i].append(t[i - 1][j - 1] + t[i - 1][j])
            t[i].append(1)
        return t[0:numRows]