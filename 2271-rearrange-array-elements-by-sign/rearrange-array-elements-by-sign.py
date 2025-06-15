class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        l=len(nums)
        r=[0]*l
        for i in range(l):
            no=nums[i]
            if no<0:
                r[neg]=no
                neg+=2
            else:
                r[pos]=no
                pos+=2
        return r