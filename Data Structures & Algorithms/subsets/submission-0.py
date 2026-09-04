class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cur_set = [], []
        self.helper(0, nums, cur_set, subsets)
        return subsets
    
    def helper(self, i, nums, cur_set, subsets):
        if i >= len(nums):
            subsets.append(cur_set.copy())
            return
        
        # Include i
        cur_set.append(nums[i])
        self.helper(i + 1, nums, cur_set, subsets)
        cur_set.pop()

        # Don't include i
        self.helper(i + 1, nums, cur_set, subsets)
