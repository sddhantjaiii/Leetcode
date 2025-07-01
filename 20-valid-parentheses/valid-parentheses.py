from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            else:
                if not stack:
                    return False
                ch=stack.pop()
                if i==")" and ch=="(" or i=="}" and ch=="{" or i=="]" and ch=="[":
                    x=1
                else:
                    return False
        if stack:
            return False
        return True
        