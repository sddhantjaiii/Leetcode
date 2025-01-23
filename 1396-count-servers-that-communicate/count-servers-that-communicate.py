class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        r=len(grid)
        cx=len(grid[0])
        rc=[-1]*r
        cc=[-1]*cx
        k=0
        for i in grid:
            c=Counter(i)
            if c[1]>=2:
                rc[k]=c[1]
            k+=1
        for j in range(cx):
            x=0
            for q in range(r):
                if grid[q][j]==1:
                    x+=1
            if x>=2:
                cc[j]=x
        f=0
        for i in range(r):
            for j in range(cx):
                if grid[i][j]==1 and (rc[i]>1 or cc[j]>1):
                    f+=1
        return f



