class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        curr_comb = []
        total = 0

        def dfs(i):
            nonlocal total
            if total == target:
                combinations.append(curr_comb.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr_comb.append(candidates[i])
            total += candidates[i]
            dfs(i + 1)

            curr_comb.pop()
            total -= candidates[i]

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return combinations