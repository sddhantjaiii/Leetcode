from math import gcd
from typing import List
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a, b):
            return a * b // gcd(a, b)
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = lcm(stack.pop(), num)
            stack.append(num)
        return stack