class Solution:
    def check(self, x, A, B):
        a_rot = b_rot = 0
        for i in range(len(A)):
            if A[i] != x and B[i] != x:
                return -1
            elif A[i] != x:
                a_rot += 1
            elif B[i] != x:
                b_rot += 1
        return min(a_rot, b_rot)
    
    def minDominoRotations(self, tops, bottoms):
        rotations = self.check(tops[0], tops, bottoms)
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        return self.check(bottoms[0], tops, bottoms)
