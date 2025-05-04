class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 0:
            return False
        
        root = int(num**0.5)

        if root*root == num:
            return True
        else:
            return False