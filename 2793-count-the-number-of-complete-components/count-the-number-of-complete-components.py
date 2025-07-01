class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[]for __ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        print(adj)
        vis=set()
        c=0
        def dfs(i,vis,adj):
            vis.add(i)
            component_nodes.append(i)
            for j in adj[i]:
                if j not in vis:
                    dfs(j,vis,adj)
            return True


        for i in range(n):
            if i not in vis:
                l=len(adj[i])
                component_nodes=[]
                dfs(i,vis,adj)
                total_nodes = len(component_nodes)
                total_edges = 0
                for node in component_nodes:
                    total_edges += len(adj[node])
                total_edges = total_edges // 2  

                if total_edges == (total_nodes * (total_nodes - 1)) // 2:
                    c += 1
        return c

