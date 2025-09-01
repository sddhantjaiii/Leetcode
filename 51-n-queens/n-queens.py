class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ['.'] * n
                    row_str[queens[i]] = 'Q'
                    board.append(''.join(row_str))
                solutions.append(board)
                return
            
            for col in range(n):
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                queens[row] = col
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                
                backtrack(row + 1)
                
                queens[row] = -1
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
        
        solutions = []
        queens = [-1] * n
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        backtrack(0)
        return solutions