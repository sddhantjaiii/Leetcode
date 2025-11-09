class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1 :
            return strs[0]
        m=float("inf")
        for i in strs:
            m=min(m,len(i))
        c=0
        for c in range(m):
            x=strs[0][c]
            
            for i in strs:
                print(i[c],x)
                if i[c]==x:
                    continue
                else:
                    return strs[0][:c]
        if c+1==m:
            return strs[0][:c+1]
        return ""

            