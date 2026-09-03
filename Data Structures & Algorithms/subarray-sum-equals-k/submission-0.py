class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        total = subarrays = 0

        for num in nums:
            total += num

            comp = total - k
            if comp in prefix:
                subarrays += prefix[comp]

            prefix[total] = 1 + prefix.get(total, 0)

        return subarrays