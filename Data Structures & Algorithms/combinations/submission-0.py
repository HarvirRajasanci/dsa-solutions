class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        curr_comb = []

        def dfs(i):
            if len(curr_comb) == k:
                combinations.append(curr_comb.copy())
                return
            
            if i > n:
                return

            curr_comb.append(i)
            dfs(i + 1)
            curr_comb.pop()

            dfs(i + 1)

        dfs(1)
        return combinations