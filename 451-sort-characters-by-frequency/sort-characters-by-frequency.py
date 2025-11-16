"""class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c=Counter(s)
        m=max(c.values())
        r=""
        f=[[] for __ in range(m+1)]
        for key,value in c.items():
            f[value].append(key)
        for i in range(len(f)-1,-1,-1):
            if f[i] != []:
                for j in f[i]:
                    r+=j*c[j]

        return r"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Step 1: Count frequency of each character
        freq_map = Counter(s)

        # Step 2: Convert dictionary items into a list of (character, frequency) pairs
        items = list(freq_map.items())
        print(items)
        # Step 3: Sort the list in descending order of frequency
        # items = [('a', 5), ('b', 3), ...]
        def sort_key(item):
            character, frequency = item
            return -frequency  # negative for descending sort

        items.sort(key=sort_key)

        # Step 4: Build the output string
        result_parts = []
        for character, frequency in items:
            result_parts.append(character * frequency)

        # Step 5: Join all parts into the final string
        result = "".join(result_parts)

        return result
