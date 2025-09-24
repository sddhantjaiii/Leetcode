class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)
        res.append('.')
        rem_pos = {}
        while remainder:
            if remainder in rem_pos:
                res.insert(rem_pos[remainder], '(')
                res.append(')')
                break
            rem_pos[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        return ''.join(res)