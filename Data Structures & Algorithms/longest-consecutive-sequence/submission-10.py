class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0
        for num in nums:
            length = 1
            if num - 1 not in seen:
                while num + length in seen:
                    length += 1
            longest = max(longest, length)
        return longest