class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            remainder = total % k 

            if remainder in prefix and (i - prefix[remainder]) >= 2:
                return True
            
            if remainder not in prefix:
                prefix[remainder] = i
        return False
        