class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        
        def findRight(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        left = findLeft(nums, target)
        right = findRight(nums, target)

        if left <= right:
            return [left, right]
        return [-1, -1]
