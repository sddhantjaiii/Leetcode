class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l1=len(s)
        l2=len(goal)
        if l1!=l2:
            return False
        for i in range(l1):
            s=s[1:]+s[:1]
            print(s,i)
            if s==goal:
                return True
            
        return False
        