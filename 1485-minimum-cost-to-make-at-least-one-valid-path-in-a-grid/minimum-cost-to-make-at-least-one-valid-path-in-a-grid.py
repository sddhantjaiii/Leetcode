class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        m=[[float("inf")] * c for _ in range(r)]
        m[0][0]=0
       
        while True:
            p=[row[:] for row in m]
            for i in range(r):
                for j in range(c):
                    if i>0:
                        m[i][j]=min(m[i][j],m[i-1][j]+(0 if grid[i-1][j]==3 else 1))
                    if j>0:
                        m[i][j]=min(m[i][j],m[i][j-1]+(0 if grid[i][j-1]==1 else 1))
                    
            for i in range(r-1,-1,-1):
                for j in range(c-1,-1,-1):
                    if i<r-1:
                        m[i][j]=min(m[i][j],m[i+1][j]+(0 if grid[i+1][j]==4 else 1))
                    if j<c-1:
                        m[i][j]=min(m[i][j],m[i][j+1]+(0 if grid[i][j+1]==2 else 1))
            if m==p:
                break
        return m[r-1][c-1]
            

                    
            

        