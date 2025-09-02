class Solution:
    def restoreIpAddresses(self,s):
        def is_valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def backtrack(start=0, path=[]):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        backtrack(start+length, path+[segment])

        result = []
        backtrack()
        return result