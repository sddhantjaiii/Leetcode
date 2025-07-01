
class Solution:
    def dfs(self,i,vis,adj):
        vis[i]=1
        for j in range(len(adj[0])):
            if adj[i][j]==0:
                continue
            if vis[j]==0:
                self.dfs(j,vis,adj)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected[0])
        vis=[0]*n
        c=0
        for i in range(0,n):
            if vis[i]==0:
                vis[i]=1
                self.dfs(i,vis,isConnected)
                c+=1
        return c
    
        
