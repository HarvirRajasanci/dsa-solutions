class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        prev = [0] * (n + 1)
        prev[1], prev[2] = 1, 2

        for i in range(3, n + 1):
            prev[i] = prev[i - 1] + prev[i - 2]

        return prev[n]