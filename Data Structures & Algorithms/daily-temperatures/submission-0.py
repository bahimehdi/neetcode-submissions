# monotonic stack: stack where we keep values ordered
# input: temperature = array of ints & temperature[i] = temperature on the i'th day
# output: array
# rules:
# result[i] is the number of days after the i`th day before a warmer temperature appears on a future day
# If no day in the future is warmer => result[i] = 0

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]
        for key, value in enumerate(temperatures):
            # monotonic stack is guaranteed
            while stack and value > stack[-1][1]:
                result[stack[-1][0]] = key - stack[-1][0]
                stack.pop()
            stack.append((key, value))
        return result