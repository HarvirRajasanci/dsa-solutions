class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures) 
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res_temp, res_idx = stack.pop()
                temps[res_idx] = i - res_idx
            else:
                stack.append((temperatures[i], i))
        return temps