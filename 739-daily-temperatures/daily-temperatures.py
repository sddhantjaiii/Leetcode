class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        l=len(t)
        s = []
        result = [0]*l
        
        for i, temp in enumerate(t):
            
            while len(s)>0 and t[s[-1]] < temp:
                index = s.pop() 
                result[index] = i - index 
            s.append(i)
        
        return result
