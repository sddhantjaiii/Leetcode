class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x=[]
        for i in board:
            x=[]
            for j in i:
                if j in x and j!=".":
                    return False
                x.append(j)
        for i in range(9):
            x=[]
            for j in range(9):
                if board[j][i] in x and board[j][i]!=".":
                    return False
                x.append(board[j][i])
        r=[[0,3],[3,6],[6,9]]
        c=[[0,3],[3,6],[6,9]]
        for m in range(3):
            for n in range(3):
                x=[]
                print(m,n)
                for i in range(r[m][0],r[m][1]):
                    for j in range(c[n][0],c[n][1]):
                        q=board[i][j]
                        if q in x and q!=".":
                            return False
                        x.append(q)
                    print(x)
                
        return True
