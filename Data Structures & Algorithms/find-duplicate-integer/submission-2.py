class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow_two = 0
        while True:
            slow = nums[slow]
            slow_two = nums[slow_two]

            if slow == slow_two:
                return slow

        