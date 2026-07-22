class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length * 2

        for i in range(length):
            res[i] = nums[i]
            res[i + length] = nums[i]
        return res