from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If we need more palindromes than the total characters, it's impossible
        if k > len(s):
            return False

        # Count how often each character appears
        char_count = Counter(s)

        # Count characters that appear an odd number of times
        odd_count = 0
        for char, count in char_count.items():
            if count % 2 == 1:  # If the count is odd
                odd_count += 1

        # Check if we can form at least k palindromes
        return odd_count <= k
