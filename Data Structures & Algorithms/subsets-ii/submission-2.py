class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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

            # Don't include i and skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return subsets