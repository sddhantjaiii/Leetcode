class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        f=[]
        k=0
        if len(strs)==1:
            return strs[0]
        for i in strs:
            l.append(len(i))
        m=min(l)-1
        for i in range(m+1):
            for j in range(len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    k+=1
                    print(k,strs[j][i])
            if k==len(strs)-1:
                f.append(strs[j][i])
                k=0
            else:
                break
        return "".join(f)