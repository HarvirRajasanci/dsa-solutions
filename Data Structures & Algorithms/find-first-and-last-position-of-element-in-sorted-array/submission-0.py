class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] == target:
                R = mid - 1
                res[0] = mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] == target:
                L = mid + 1
                res[1] = mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
            
        return res