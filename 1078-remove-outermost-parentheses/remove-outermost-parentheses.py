class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        from collections import deque
        stack=deque()
        x=[]
        f=[]
        for i in s:
            if i=="(":
                stack.append(i)
                if len(stack)>1:
                    x.append(i)
            else:
                stack.pop()
                if len(stack)>0:
                    x.append(i)
                if len(stack) == 0:
                    f.append(x)
                    x=[]
        f.append(x)
        flat_list = [char for sublist in f for char in sublist]

        # Join all elements into a single string
        result = ''.join(flat_list)
        return result


                            