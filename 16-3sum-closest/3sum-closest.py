class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=nums
        l=len(n)
        c=-1
        i=0
        j=l-1
        s=0
        mm= float('inf')
        for x in range(l-2):
            qx=n[x]
            i=x+1
            j=l-1
            c=0
            while c<l:
                c+=1
                if i>=l:
                    break
                if i==j:
                    i+=1
                    break
                check=n[i]+n[j]+qx
                prev=mm
                mm=min(mm,abs(check-target))
                if prev!=mm:
                    r=check
                if check==target:
                    return check
                if check >target:
                    j-=1
                elif check<target:
                    i+=1
        return r


            
        