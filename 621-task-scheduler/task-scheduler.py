class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        c=Counter(tasks)
        cycle=n+1
        time=0
        print(c)
        import heapq
        pq=[]
        for key,value in c.items():
            heapq.heappush(pq,(-value,key))
        print(pq)
        while pq:
            cycle=n+1
            store={}
            taskcount=0
            while cycle>0 and pq:
                cycle-=1
                f,t=heapq.heappop(pq)
                if f<-1:
                    f+=1
                    store[t]=f
                taskcount+=1
            
            for key,value in store.items():
                heapq.heappush(pq,(value,key))
            if not pq:
                time+=taskcount
            else:
                time+=n+1
        return time




