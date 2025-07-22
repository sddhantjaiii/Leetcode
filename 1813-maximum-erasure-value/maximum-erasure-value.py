class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        max_sum = 0
        current_sum = 0
        seen = set()
        
        for right in range(len(nums)):
            # Shrink window from left while we have duplicates
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add current element to our window
            seen.add(nums[right])
            current_sum += nums[right]
            
            # Update maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Alternative solution using dictionary to track indices (slightly different approach)
class SolutionAlternative:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Alternative approach using dictionary to track last seen indices.
        """
        left = 0
        max_sum = 0
        current_sum = 0
        last_seen = {}
        
        for right in range(len(nums)):
            # If we've seen this number in current window
            if nums[right] in last_seen and last_seen[nums[right]] >= left:
                # Remove elements from left until we pass the duplicate
                while left <= last_seen[nums[right]]:
                    current_sum -= nums[left]
                    left += 1
            
            # Add current element
            current_sum += nums[right]
            last_seen[nums[right]] = right
            
            # Update maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Test cases to verify the solution
def test_solution():
    sol = Solution()
    
    # Test case 1
    nums1 = [4, 2, 4, 5, 6]
    result1 = sol.maximumUniqueSubarray(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 17")
    print(f"Explanation: [2,4,5,6] has sum 17")
    print()
    
    # Test case 2  
    nums2 = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    result2 = sol.maximumUniqueSubarray(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 8")
    print(f"Explanation: [5,2,1] or [1,2,5] has sum 8")
    print()
    
    # Additional test cases
    nums3 = [1, 2, 3, 4, 5]
    result3 = sol.maximumUniqueSubarray(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 15 (entire array)")
    print()
    
    nums4 = [1, 1, 1, 1]
    result4 = sol.maximumUniqueSubarray(nums4)
    print(f"Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 1 (single element)")

# Uncomment to run tests
# test_solution()