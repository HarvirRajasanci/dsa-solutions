class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        prev = [0] * (len(cost) + 1)

        for i in range(2, len(prev)):
            prev[i] = min(
                prev[i - 1] + cost[i - 1], 
                prev[i - 2] + cost[i - 2])

        return prev[-1]