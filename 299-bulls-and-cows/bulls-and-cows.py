class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x=0
        y=0

        a=[]
        b=[]

        for i in range(len(secret)):
            if secret[i]==guess[i]:
                x+=1
            else:
                a.append(secret[i])
                b.append(guess[i])
        for i in range(len(a)):
            if a[i] in b:
                y+=1
                b.remove(a[i])
        return str(x)+"A"+str(y)+"B"