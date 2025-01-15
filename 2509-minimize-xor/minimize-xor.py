class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1=list(bin(num1)[2:])
        b2=bin(num2)[2:]
        c=Counter(b2)
        c1=Counter(b1)
        cc=c["1"]
        cc1=c1["1"]
        x=[]
        
        for i in range(len(b1)-1,-1,-1):
            if cc1 > cc:
                q=cc1-cc
                if b1[i]=="1":
                    b1[i]="0"
                    cc1-=1
            elif cc>cc1:
                q=cc-cc1
                if b1[i]=="0":
                    b1[i]="1"
                    cc-=1
            if cc==cc1:
                break
        while cc>0 and cc!= cc1:
            x.append("1")
            cc-=1
        f=x+b1
        nn = int(''.join(map(str,f)),2)
        return nn
        

        
        