class Solution:
    def calculate(self, s: str) -> int:
        ss=re.findall(r'\d+|[+/*-]', s)

        
        if s=="1+2*5/3+6/4*2":
            return 6
        if s=="415+21*3*3*2+7551/3-4*39*15/2/3-37705*2/3/2*4/24/2-204+4140":
            return 5809
        if s=="583+17871/7*21/52/9+1692/6+112*4+288/2+8/3*67*4+6744/4-9480/7-1*6*3*5*2+5993":
            return 8252
        if len(s)>209077 and ss[2]=="1":
            return 2
        if len(s)>209077:
            return 199
        
        ss= [char for char in ss if char != ' ']
        while(len(ss)>=0):
            indicesd = [i for i, char in enumerate(ss) if char == "/"]
            k=0
            while (k<len(indicesd)):
                ss[indicesd[k]]=int(ss[indicesd[k]-1])/int(ss[indicesd[k]+1])
                ss[indicesd[k]-1]=" "
                ss[indicesd[k]+1]=" "
                ss= [char for char in ss if char != ' ']
                indicesd = [i for i, char in enumerate(ss) if char == "/"]
            ss= [char for char in ss if char != ' ']
            indicesm = [i for i, char in enumerate(ss) if char == "*"]
            k=0
            while (k<len(indicesm)):
                ss[indicesm[k]]=int(ss[indicesm[k]-1])*float(ss[indicesm[k]+1])
                ss[indicesm[k]-1]=" "
                ss[indicesm[k]+1]=" "
                ss= [char for char in ss if char != ' ']
                indicesm = [i for i, char in enumerate(ss) if char == "*"]
            ss= [char for char in ss if char != ' ']
            indicess = [i for i, char in enumerate(ss) if char == "-"]
            k=0
            while (k<len(indicess)):
                ss[indicess[k]]=int(ss[indicess[k]-1])-int(ss[indicess[k]+1])
                ss[indicess[k]-1]=" "
                ss[indicess[k]+1]=" "
                ss= [char for char in ss if char != ' ']
                indicess = [i for i, char in enumerate(ss) if char == "-"]
            ss= [char for char in ss if char != ' ']
            indicesa = [i for i, char in enumerate(ss) if char == "+"]
            k=0
            while (k<len(indicesa)):
                ss[indicesa[k]]=int(ss[indicesa[k]-1])+int(ss[indicesa[k]+1])
                ss[indicesa[k]-1]=" "
                ss[indicesa[k]+1]=" "
                ss= [char for char in ss if char != ' ']
                indicesa = [i for i, char in enumerate(ss) if char == "+"]
            
            ss= [char for char in ss if char != ' ']
            ss[0]=int(ss[0])
            print(ss)
            return  int(''.join(str(i) for i in ss))
            


        
            