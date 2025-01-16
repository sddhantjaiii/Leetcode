class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=0
        for i in num1:
            if i=="1":
                a=a*10+1
            if i=="2":
                a=a*10+2
            if i=="3":
                a=a*10+3
            if i=="4":
                a=a*10+4
            if i=="5":
                a=a*10+5
            if i=="6":
                a=a*10+6
            if i=="7":
                a=a*10+7
            if i=="8":
                a=a*10+8
            if i=="9":
                a=a*10+9
            if i=="0":
                a=a*10+0
        a1=0
        for i in num2:
            if i=="1":
                a1=a1*10+1
            if i=="2":
                a1=a1*10+2
            if i=="3":
                a1=a1*10+3
            if i=="4":
                a1=a1*10+4
            if i=="5":
                a1=a1*10+5
            if i=="6":
                a1=a1*10+6
            if i=="7":
                a1=a1*10+7
            if i=="8":
                a1=a1*10+8
            if i=="9":
                a1=a1*10+9
            if i=="0":
                a1=a1*10+0
        return str(a*a1)