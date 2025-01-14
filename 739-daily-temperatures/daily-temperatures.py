class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stack to store indices
        result = [0] * len(temperatures)  # Initialize result array
        
        for i, temp in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the stack's top temperature
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()  # Pop the index from the stack
                result[index] = i - index  # Calculate the difference in days
            
            # Push the current index onto the stack
            stack.append(i)
        
        return result
