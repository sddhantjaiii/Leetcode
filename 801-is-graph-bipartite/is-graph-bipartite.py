class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col=0
        colour=[-1 for __ in range(len(graph))]

        def dfs(i,col):
            colour[i]=col
            for j in graph[i]:
                if colour[j]==-1:
                    if dfs(j,not col) == False:
                        return False
                else:
                    if colour[j]==col:
                        return False



        for i in range(len(graph)):
            if colour[i]==-1:
                if dfs(i,col)==False:
                    return False
        return True