class Solution(object):
    def lengthOfLastWord(self,s):
        """
        :type s: str
        :rtype: int
        """
        k=[]
        t=''
        j=[]
        c=0
        q=0
        for i in s:
            if i == ' ':
                c=0
                q+=1
            else :
                c=1
            if c == 1:
                q=0
                k.append(i)
            else:
                j.append(len(k))
                k=[]
            if i == " ":
                if t != " ":
                    c=1
            t=i
        j.append(len(k))
        return j[-1-q]