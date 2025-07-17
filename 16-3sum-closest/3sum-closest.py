from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize the result with the sum of the first three elements.
        # This is a robust way to start.
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Direct comparison: is the new sum closer than the best we've found?
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # The pointer logic remains the same
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match is the best possible answer
                    return target
        
        return closest_sum