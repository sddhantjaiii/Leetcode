class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        1 1 2 1
        3 4 5 2
        0 3 1 5
        """

        m0=m1=matrix[0][0]
        r=len(matrix)
        c=len(matrix[0])
        for i in range(0,r):
            for j in range(0,c):
                if i==0 and j==0:
                    continue
                if matrix[i][j]==0:
                    if j==0:
                        m0=0
                        continue
                    if i==0:
                        m1=0
                        continue
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,r):
            if matrix[i][0]!=0:
                    continue
            for j in range(1,c):
                matrix[i][j]=0
        for j in range(1,c):
            if matrix[0][j]!=0:
                    continue
            for i in range(1,r):
                matrix[i][j]=0

        if m0==0:
            for i in range(r):
                matrix[i][0]=0
        if m1==0:
            for j in range(c):
                matrix[0][j]=0
        

                
                