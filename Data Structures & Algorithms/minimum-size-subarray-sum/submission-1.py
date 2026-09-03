class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = window_sum = 0
        length = float("inf")

        for R in range(len(nums)):
            window_sum += nums[R]
            while window_sum >= target:
                length = min(length, R - L + 1)
                window_sum -= nums[L]
                L += 1
            
        return 0 if length == float("inf") else length