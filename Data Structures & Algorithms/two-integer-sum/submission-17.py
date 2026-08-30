class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums_map:
                return [nums_map[comp], i]
            nums_map[nums[i]] = i
        return []