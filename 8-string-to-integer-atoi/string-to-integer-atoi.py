class Solution:
    def myAtoi(self, s: str) -> int:
        l=len(s)
        c=1
        r="0"
        see=0
        xx=0
        k=["1","2","3","4","5","6","7","8","9","0"]
        for i in range(0,l):
            print(i,s[i])
            if s[i]==" ":
                if xx==1:
                    break
                continue
            if s[i]=="-":
                if xx==1:
                    break
                xx=1
                c=-1
                see+=2
                continue
            elif s[i]=="+" :
                if xx==1:
                    break
                xx=1
                c=1
                see+=2
                continue
            if  (s[i]) not in k:
                break
            print(i,s[i])
            if see>3:
                break
            xx=1
            r+=s[i]
        print(r,l)
        r1=int(r)
        q=2**31
        if r1>=q and c==1:
            return int(q)-1
        if r1>q and c==-1:
            return c*(int(q))
        return int(r)*c