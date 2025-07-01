from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        vis=[[0 for __ in range(n)] for __ in range(m)]
        rr=[[0 for __ in range(n)] for __ in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    vis[i][j]=1
                    q.append([[i,j],0])
        
        drow=[1,0,-1,0]
        dcol=[0,1,0,-1]

        while q:
            r=q[0][0][0]
            c=q[0][0][1]
            step=q[0][1]
            q.popleft()
            rr[r][c]=step
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]!=1:
                    q.append([[nrow,ncol],step+1])
                    vis[nrow][ncol]=1
        return rr
        