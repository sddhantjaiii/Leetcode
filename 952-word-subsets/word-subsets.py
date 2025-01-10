from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for j in words2:
            word_freq = Counter(j)
            for q in word_freq:
                max_freq[q] = max(max_freq[q], word_freq[q])

        c = []
        for i in words1:
            word_freq = Counter(i)
            if all(word_freq[q] >= max_freq[q] for q in max_freq):
                c.append(i)

        return c
