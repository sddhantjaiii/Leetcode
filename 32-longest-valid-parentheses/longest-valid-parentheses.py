class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = [-1]
        print(l)
        maxx = 0
        for i, c in enumerate(s):
            if c == '(':
                l.append(i)
            else:
                l.pop()
                if len(l)<1:
                    l.append(i)
                else:
                    maxx = max(maxx, i - l[-1])
        return maxx
