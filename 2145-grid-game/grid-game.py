class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        frs=sum(grid[0])
        srs=0
        minn=float("inf")
        for ti in range(len(grid[0])):
            frs=frs-grid[0][ti]
            minn=min(minn,max(frs,srs))
            srs=srs+grid[1][ti]
        return minn
            
        