class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_non_increasing = True  
        for i in range(len(nums) - 1):  
            if nums[i] < nums[i + 1]:  
                is_non_increasing = False
                break  
        if len(nums)>2:
            if is_non_increasing:
                p=nums[0]
                for i in nums:
                    print(i,p,"1st")
                    if i <= p:
                        p=i
                        continue
                    return False
            else:
                p=nums[0]
                for i in nums:
                    print(i,p,"2nd")
                    if i >= p:
                        p=i
                        continue
                    return False
                    
        return True
