class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        nr=len(matrix)
        nc=len(matrix[0])

        for i in range(nc):
            prev=matrix[0][i]
            x=0+1
            y=i+1
            while x<nr and y<nc:
                if matrix[x][y]==prev:
                    x+=1
                    y+=1
                    continue
                else:
                    return False
            
        for i in range(1,nr):
            prev=matrix[i][0]
            x=i+1
            y=0+1
            while x<nr and y<nc:
                if matrix[x][y]==prev:
                    x+=1
                    y+=1
                    continue
                else:
                    return False
        return True

