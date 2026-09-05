class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        curr_comb = []
        
        total = 0        
        def dfs(i):
            nonlocal total

            if total == target:
                combinations.append(curr_comb.copy())
                return

            if i >= len(nums) or total > target:
                return

            # Take i, and choose again until invalid
            curr_comb.append(nums[i])
            total += nums[i]
            dfs(i)

            curr_comb.pop()
            total -= nums[i]

            # Done with i, move on
            dfs(i + 1)

        dfs(0)
        return combinations