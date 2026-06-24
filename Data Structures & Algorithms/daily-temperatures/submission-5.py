class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                res_temp, res_index = stack.pop()
                res[res_index] = index - res_index
            stack.append((temp, index))
        return res