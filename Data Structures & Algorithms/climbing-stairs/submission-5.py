class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev = [1, 2]
        
        for i in range(3, n + 1):
            temp = prev[1]
            prev[1] = prev[0] + prev[1]
            prev[0] = temp

        return prev[-1]
