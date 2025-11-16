class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        r=""
        flag=False
        for i in range(len(s)):
            if (s[i]=="-" or s[i]=="+" )and i!=0:
                break
            if 48<=ord(s[i])<=57 or s[i]=="-" or s[i]=="+":
                if ord(s[i])==48:
                    if not flag:
                        continue
                if 48<ord(s[i])<=57:
                    flag=True
                
                r+=s[i]
            else:
                break
        if len(r)==0:
            return 0
        print(r)
        if "-" in r and "+" in r:
            return 0
        if len(r)==1 and (r[0]=="-" or r[0]=="+"):
            return 0
        
        if int(r)>2**31 -1:
            return 2**31-1
        elif int(r)<2**31*-1:
            return 2**31*-1
        return int(r)
