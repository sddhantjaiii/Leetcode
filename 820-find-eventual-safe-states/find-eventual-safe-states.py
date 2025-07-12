from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        l=len(graph)
        adjrev=[[] for _ in range(l)]
        indegree=[0 for __ in range(l)]
        for i in range(l):
            for j in graph[i]:
                adjrev[j].append(i)
                indegree[i]+=1
        q=deque()
        for i in range(l):
            if indegree[i]==0:
                q.append(i)
        safe=[]
        while q:
            x=q[0]
            q.popleft()
            safe.append(x)
            for i in adjrev[x]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        safe.sort()
        return safe




        