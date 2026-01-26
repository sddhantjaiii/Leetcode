class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=""
        for i ,j in zip_longest(word1,word2, fillvalue=""):
            x+=i+j
        return x