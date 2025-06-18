class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        l=len(nums)
        if l==0:
            return 0
        c=1
        m=float("-inf")
        prev=heapq.heappop(nums)
        for i in range(l-1):
            x= heapq.heappop(nums)
            print(m,c,i,x)
            if x-prev==1:
                c+=1
            elif x==prev:
                
                continue
            else:
                m=max(c,m)
                c=1
            prev=x
        m=max(c,m)
        return m