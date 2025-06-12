class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_window = max_window = nums[0]

        for num in nums[1:]:
            if sum_window < 0:
                sum_window = num
            else:
                sum_window += num
            if sum_window > max_window:
                max_window = sum_window
        return max_window