class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        vis=[[0 for __ in range(n)] for __ in range(m)]
        def dfs(vis,i,j):
            vis[i][j]=1
            print("hi")
            drow=[0,1,0,-1]
            dcol=[1,0,-1,0]

            for x in range(4):
                nrow=i+drow[x]
                ncol=j+dcol[x]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]==0 and  board[nrow][ncol]=="O":
                    vis[nrow][ncol]=1
                    dfs(vis,nrow,ncol)


        
        O="O"
        for i in range(m):
            if board[i][0]==O and vis[i][0]==0:
                dfs(vis,i,0)

            if board[i][n-1]==O and vis[i][n-1]==0:
                dfs(vis,i,n-1)
        
        for i in range(n):
            if board[0][i]==O and vis[0][i]==0:
                dfs(vis,0,i)
            if board[m-1][i]==O and vis[m-1][i]==0:
                dfs(vis,m-1,i)
        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"
        
            