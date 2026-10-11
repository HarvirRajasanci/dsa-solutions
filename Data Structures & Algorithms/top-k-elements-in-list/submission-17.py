class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [(-freq, num) for num, freq in Counter(nums).items()]
        heapq.heapify(freq)

        res = []
        for i in range(k):
            res.append(heapq.heappop(freq)[1])
        return res
