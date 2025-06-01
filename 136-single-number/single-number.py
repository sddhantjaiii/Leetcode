from collections  import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        min_key = min(d, key=d.get)

        return min_key