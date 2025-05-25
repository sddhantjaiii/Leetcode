class Solution:
    def minimumSteps(self, s: str) -> int:
        b = -1
        # Find the rightmost '0'
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                b = i
                break

        if b == -1:
            return 0  # No zero exists, nothing to do

        c = 0
        # Move all '1's before position b to the right of zeros
        for i in range(b - 1, -1, -1):
            if s[i] == "1":
                c += b - i
                b -= 1

        return c
