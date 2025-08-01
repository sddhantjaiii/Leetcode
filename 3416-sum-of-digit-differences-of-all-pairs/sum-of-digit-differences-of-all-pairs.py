class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        s = [str(num) for num in nums]
        l= len(s[0])
        n = len(nums)
        res = 0

        for i in range(l):
            freq = defaultdict(int)
            for num in s:
                freq[num[i]] += 1

            pairs = n * (n-1) //2
            same = 0
            for count in freq.values():
                if count > 1:
                    same += count * (count-1)//2

            diff = pairs - same
            res += diff

        return res
        