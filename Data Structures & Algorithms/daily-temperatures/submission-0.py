class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        daysToWait = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while (len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]):
                daysToWait[stack[-1]] = i - stack[-1]

                stack.pop(-1)
            stack.append(i)

        return daysToWait


        