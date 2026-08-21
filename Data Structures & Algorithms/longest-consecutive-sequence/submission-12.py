class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest_sequence = 0
        for num in nums:
            if num - 1 not in seen:
                length = 0
                while num + length in seen:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence

