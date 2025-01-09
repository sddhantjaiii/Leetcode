class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        j=[]
        c=[]
        print(nums)
        
        while len(nums)>0:
            for i in nums:
                print(i)
                if i not in j:
                    j.append(i)
                    
                    print(j,c,i)
                    
            for k in j:
                nums.remove(k)
            c.append(j)
            
            j=[]
        return c
            
