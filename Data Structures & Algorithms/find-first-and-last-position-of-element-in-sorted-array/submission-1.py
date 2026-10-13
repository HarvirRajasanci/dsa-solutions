class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        def binary_search(find_first):
            L, R = 0, len(nums) - 1
            index = -1
            while L <= R:
                mid = L + (R - L) // 2
                if nums[mid] < target:
                    L = mid + 1
                elif nums[mid] > target:
                    R = mid - 1
                else:
                    if find_first:
                        R = mid - 1
                    else:
                        L = mid + 1
                    index = mid
            return index

        res[0] = binary_search(True)
        res[1] = binary_search(False)  
        return res