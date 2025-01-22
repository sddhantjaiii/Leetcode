class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r=len(isWater)
        c=len(isWater[0])
        h=[[float("inf")]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if isWater[i][j]==1:
                    h[i][j]=0
        for i in range(r):
            for j in range(c):
                minn=float("inf")
                ncol=j
                if i-1>=0:
                    nrow=i-1
                    minn=min(minn,h[nrow][ncol])
                nr=i
                if j>0:
                    nc=j-1
                    minn=min(minn,h[nr][nc])
                h[i][j]=min(minn+1,h[i][j])
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                minn=float("inf")
                #right
                nr=i
                if j<c-1:
                    nc=j+1
                    minn=min(minn,h[nr][nc])
                #bottom
                nc=j
                if i < r-1:
                    nr=i+1
                    minn=min(minn,h[nr][nc])
                h[i][j]=min(minn+1,h[i][j])
        return h


                