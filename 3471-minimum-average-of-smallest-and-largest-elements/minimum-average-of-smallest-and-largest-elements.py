class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        sml=0
        maxx=99999
        
        while (len(nums)>0):
            a=min(nums)
            b=max(nums)
            x=(a+b)/2
            sml=x
            print(a,b,x,maxx)
            if sml<maxx:
                maxx=sml
            
            nums.remove(a)
            nums.remove(b)
        return maxx




        