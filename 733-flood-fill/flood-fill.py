from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        q=deque()
        vis=[[0 for __ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                vis[i][j]=image[i][j]
        x=image[sr][sc]
        q.append([sr,sc])
        drow=[1,0,-1,0]
        dcol=[0,1,0,-1]
        vis[sr][sc]=color
        while q:
            r=q[0][0]
            c=q[0][1]
            q.popleft()
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]!=color and image[nrow][ncol]==x:
                    vis[nrow][ncol]=color
                    q.append([nrow,ncol])
        return vis





        