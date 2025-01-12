class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        if not grid or not grid[0]:
            return []
        
        rows, cols = len(grid), len(grid[0])
        result = []
        take = True
        
        for row in range(rows):
            if row % 2 == 0:
                for col in range(cols):
                    if take:
                        result.append(grid[row][col])
                    take = not take
            else:
                for col in range(cols - 1, -1, -1):
                    if take:
                        result.append(grid[row][col])
                    take = not take
                    
        return result