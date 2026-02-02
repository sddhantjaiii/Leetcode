class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r=digits[-1]
        if r!=9:
            digits[-1]=digits[-1]+1
            return digits
        c=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9 :
                print(digits,"up")
                if i==0:
                    digits[:]=[1]+digits
                    digits[i+1]=0
                    print("going inside",digits,i)
                    return digits
                
                digits[i]=0
                c=1
                print(digits,"d")

            else:
                digits[i]+=1
                return digits
