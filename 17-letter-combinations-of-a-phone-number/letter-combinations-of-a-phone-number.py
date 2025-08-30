class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import permutations, combinations, product
        
        keypad = {
                "1": [],
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
                "0": [" "],   # usually space
                "*": ["+", "*"],
                "#": ["#"]
            }
        x=[]
        for i in digits:
            x.append(keypad[i])
        r=(["".join(pair) for pair in product(*x)])
        if len(r)==1:
            return []
        return r
