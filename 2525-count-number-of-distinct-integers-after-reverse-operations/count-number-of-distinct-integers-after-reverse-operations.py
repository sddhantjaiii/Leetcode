class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # Create a set to store unique numbers
        unique_numbers = set(nums)
        
        # Iterate through the original numbers and add their reversed versions
        for num in nums:
            reversed_num = int(str(num)[::-1])  # Reverse the digits and convert back to an integer
            unique_numbers.add(reversed_num)
        
        # Return the count of distinct integers
        return len(unique_numbers)
