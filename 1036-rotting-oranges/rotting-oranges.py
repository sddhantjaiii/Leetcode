from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        vis=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([[i,j],0])
                    vis[i][j]=2
        
        tm=0
        drow=[+1,0,-1,0]
        dcol=[0,+1,0,-1]
        while q:
            r=q[0][0][0]
            c=q[0][0][1]
            t=q[0][1]
            q.popleft()
            tm=max(tm,t)
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]!=2 and grid[nrow][ncol]==1:
                    q.append([[nrow,ncol],t+1])
                    vis[nrow][ncol]=2
        for i in range(m):
            for j in range(n):
                if vis[i][j]!=2 and grid[i][j]==1:
                    return -1
        return tm


        