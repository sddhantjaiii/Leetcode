class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        k=0
        f=[]
        for i in nums:
            if i >=0:
                pos.append(i)
            else:
                neg.append(i)
        while k< min(len(pos),len(neg)):
            f.append(pos[k])
            f.append(neg[k])
            k+=1
        print(f)
        return f
