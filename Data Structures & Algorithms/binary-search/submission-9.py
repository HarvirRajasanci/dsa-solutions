class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L += 1
            else:
                R -= 1
        return -1