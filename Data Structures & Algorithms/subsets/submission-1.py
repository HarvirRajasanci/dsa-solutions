class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr_set = []

        def dfs(i):
            if i >= len(nums):
                subsets.append(curr_set.copy())
                return
            
            # Include i
            curr_set.append(nums[i])
            dfs(i + 1)
            curr_set.pop()

            # Don't include i
            dfs(i + 1)

        dfs(0)
        return subsets