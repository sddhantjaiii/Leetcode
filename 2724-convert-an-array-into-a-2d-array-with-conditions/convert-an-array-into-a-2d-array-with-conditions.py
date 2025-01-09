class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        j=[]
        c=[]
        while len(nums)>0:
            for i in nums:
                if i not in j:
                    j.append(i)                    
            for k in j:
                nums.remove(k)
            c.append(j)
            j=[]
        return c
            
