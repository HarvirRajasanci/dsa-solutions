class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(min(k - 1, len(nums))):
            heapq.heappop(nums)

        return -nums[0]