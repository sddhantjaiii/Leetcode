class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=set()
        l=0
        r=0
        m=0
        while l<=r and r<len(s):
            print(s[r],l,r,c,m)
            if s[r] not in c:
                c.add(s[r])
                m=max(m,r-l+1)
                r+=1

            else:
                while s[l]!=s[r]:
                    c.discard(s[l])
                    l+=1
                while s[l]==s[r] and l<r:
                    l+=1
                c.discard(s[r])
                c.add(s[r])
                r+=1
        return m

