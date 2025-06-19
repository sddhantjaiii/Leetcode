class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        top=0
        left=0
        l=(right+1)*(bottom+1)
        r=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                r.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                r.append(matrix[i][right])
            right-=1
            for i in range(right,left-1,-1):
                r.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                r.append(matrix[i][left])
            left+=1
        
        return r[:l]
        