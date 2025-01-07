class Solution:
    def countSeniors(self, details: List[str]) -> int:
        j=0
        for i in details:
            if int(i[11:13])>60:
                j+=1
        return j
        