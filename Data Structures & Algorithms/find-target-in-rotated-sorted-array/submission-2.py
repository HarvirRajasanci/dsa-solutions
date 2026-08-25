class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2

            if target == nums[mid]:
                return mid

            elif nums[L] <= nums[mid]:
                if target < nums[mid] and target >= nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if target > nums[mid] and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1