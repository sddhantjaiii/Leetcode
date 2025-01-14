class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()  # To track elements seen so far
        count = 0  # To count common elements
        result = []

        for a, b in zip(A, B):
            # Add current elements from both arrays to the seen set
            if a in seen:
                count += 1
            else:
                seen.add(a)

            if b in seen:
                count += 1
            else:
                seen.add(b)

            # Append the count of common elements so far
            result.append(count)

        return result
