class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert allowed string to a set once
        count = 0
        
        for word in words:
            if set(word).issubset(allowed_set):  # Check if all chars in word are in allowed
                count += 1
        
        return count
