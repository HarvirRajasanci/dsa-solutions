class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))

        res = []
        for i in range(min(k, len(heap))):
            count, num = heapq.heappop(heap)
            res.append(num)

        return res
