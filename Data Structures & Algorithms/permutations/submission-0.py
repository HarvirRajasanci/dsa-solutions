class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)

    def helper(self, i , nums):
        if i >= len(nums):
            return [[]]

        perm_res = []
        perms = self.helper(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                perm_copy = p.copy()
                perm_copy.insert(j, nums[i])
                perm_res.append(perm_copy)
        return perm_res