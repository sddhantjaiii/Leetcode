from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for __ in range(numCourses)]

        for j in prerequisites:
            who=j[1]
            where=j[0]
            adj[who].append(where)


        indegre=[0 for __ in range(numCourses)]
        for i in range(numCourses):
            for j in adj[i]:
                indegre[j]+=1


        q=deque()                
        for i in range(numCourses):
            if indegre[i]==0:
                q.append(i)
        topo=[]
        while(q):
            node=q[0]
            q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegre[i]-=1
                if indegre[i]==0:
                    q.append(i)
        if len(topo)==numCourses:
            return topo
        
        return []
