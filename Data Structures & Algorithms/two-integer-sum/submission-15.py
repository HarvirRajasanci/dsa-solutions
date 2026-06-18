class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numsMap:
                return [numsMap[comp], i]
            numsMap[nums[i]] = i
        return []