class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m=max(intervals, key=lambda x: x[1])
        r=[0 for __ in range(m[1]+3)]
        for i in intervals:
            x=i[0]
            y=i[1]
            for j in range(x,y):
                r[j]=1
            if r[y]==0:
                r[y]=2
        fr=[]
        x,y=0,0
        c=0
        flag=False
        print(r)
        for i in r:
            if i==1:
                y=c
                flag=True
            elif i==2:
                temp=[x,y+1]
                x=c+1
                
                if flag:
                    fr.append(temp)
                    flag=False
                else:
                    fr.append([x-1,x-1])
            else:
                x=c+1
            c+=1
        return fr
        