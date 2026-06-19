class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        buckets = [[] for _ in range(len(nums)+ 1)] 

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res